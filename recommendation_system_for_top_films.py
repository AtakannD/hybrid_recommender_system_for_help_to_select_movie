import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

# Task 1.1
movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
df = movie.merge(rating, how="left", on="movieId")

# Task 1.2
rating_counts = pd.DataFrame(df["title"].value_counts())
elected_movies = rating_counts[rating_counts["title"] <= 1000].index
selected_movies = df[~df["title"].isin(elected_movies)]

# Task 1.3
user_movie_df = selected_movies.pivot_table(index=['userId'], columns=['title'], values='rating')


# Task 1.4


def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
    rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    rating_counts = pd.DataFrame(df["title"].value_counts())
    elected_movies = rating_counts[rating_counts["title"] <= 1000].index
    selected_movies = df[~df["title"].isin(elected_movies)]
    user_movie_df = selected_movies.pivot_table(index=['userId'], columns=['title'], values='rating')
    return user_movie_df


user_movie_df = create_user_movie_df()

# Task 2.1
random_user = int(pd.Series(user_movie_df.index).sample(1, random_state=45).values)

# Task 2.2
random_user_df = user_movie_df[user_movie_df.index == random_user]

# Task 2.3
random_user_df.isnull().sum()
movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()

# Task 3.1
movies_watched_df = user_movie_df[movies_watched]

# Task 3.2
user_movie_count = movies_watched_df.T.notnull().sum()
user_movie_count = user_movie_count.reset_index()
user_movie_count.columns = ["userId", "movie_count"]

# Task 3.3

perc = len(movies_watched) * 60 / 100
users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]

# Task 4.1

final_df = pd.concat([movies_watched_df[movies_watched_df.index.isin(users_same_movies)],
                      random_user_df[movies_watched]])

# Task 4.2
corr_df = final_df.T.corr().unstack().sort_values().drop_duplicates()
corr_df = pd.DataFrame(corr_df, columns=["corr"])
corr_df.index.names = ['user_id_1', 'user_id_2']
corr_df = corr_df.reset_index()

# Task 4.3
top_users = corr_df[(corr_df['user_id_1'] == random_user) & (corr_df["corr"] >= 0.65)][
    ["user_id_2", "corr"]].reset_index(drop=True)
top_users = top_users.sort_values(by='corr', ascending=False)
top_users.rename(columns={"user_id_2": "userId"}, inplace=True)
top_users_ratings = top_users.merge(rating[["userId", "movieId", "rating"]], how='inner')
top_users_ratings = top_users_ratings[top_users_ratings["userId"] != random_user]

# Task 5.1
top_users_ratings["weighted_rating"] = top_users_ratings['corr'] * top_users_ratings['rating']

# Task 5.2
recommendation_df = top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})
recommendation_df = recommendation_df.reset_index()

# Task 5.3
movies_to_be_recommend = recommendation_df[recommendation_df["weighted_rating"] > 3.5]. \
    sort_values('weighted_rating', ascending=False)
highly_recommend = movies_to_be_recommend.merge(movie[["movieId", "title"]])["title"][0:5]


# *Item Based Recommendation*

# Task 1
movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
user = int(pd.Series(user_movie_df.index).sample(1, random_state=45).values)
movie_id = rating[(rating["userId"] == user) & (rating["rating"] == 5.0)]. \
               sort_values(by="timestamp", ascending=False)["movieId"][0:1].values[0]
movie_df = user_movie_df[movie[movie["movieId"] == movie_id]["title"].values[0]]
user_movie_df.corrwith(movie_df).sort_values(ascending=False).head(10)
itemBased_movie_recommendation = user_movie_df.corrwith(movie_df).sort_values(ascending=False)
wanted_films = itemBased_movie_recommendation[1:6].index

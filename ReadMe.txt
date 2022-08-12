*Hybrid Recommender System*


1. Business Problem

Make 10 movie recommendations for the user whose ID is given, using the item-based and user-based recommender methods.


2. Story of Dataset

The dataset is provided by MovieLens, a movie recommendation service. It contains the rating scores for these 
movies along with the movies. It contains 20,000,263 ratings across 27,278 movies. This dataset was created on 
October 17, 2016. It includes 138,493 users and data from 09 January 1995 to 31 March 2015. Users are randomly 
selected. It is known that all selected users voted for at least 20 movies.


3. Variables of Dataset

movie.csv : 
	movieId: Unique movie number.
	title: Movie name
	genres:genre
	
rating.csv: 
	userid: Unique user number. (UniqueID)
	movieId: Unique movie number. (UniqueID)
	rating: The rating given to the movie by the user
	timestamp: Date of evaluation


Task 1: Preparing Data


	Step 1: Adding the movie names and genre of the Ids to the rating dataset from the movie dataset.

	Step 2: Films that do not receive enough votes in the evaluation are removed from the dataset.

	Step 3: Creating userid-movieId pivot table

	Step 4: Functionalize the process.


Task 2: Determining the Movies Watched by the User to Make a Suggestion


	Step 1: Selecting random userid.

	Step 2: Creating a new dataframe consisting of observation units of the selected user.

	Step 3: Assigning the movies voted by the selected users to a new list.

Task 3: Accessing Data and Ids of Other Users Watching the Same Movies


	Step 1: Creating a new dataframe of the movies watched by the selected user.

	Step 2: Creating a new dataframe that contains the information of how many movies each user has watched 
	that the selected user has watched.

	Step 3: Creating a list of the user IDs of the people who watched most of the movies that the selected users voted for.


Task 4: Determining the Users to be Suggested and the Users Most Similar to the User


	Step 1: Filtering the dataframe in 3.1 so that the ids of the users that are similar to the selected 
	user in the list created in 3.3 are found.

	Step 2: Creating a new dataframe where users' correlations with each other will be found.

	Step 3: Creating a new dataframe by filtering out users with high correlation with the selected user.


Task 5: Calculating the Weighted Average Recommendation Score and Keeping the Top 5 Movies

	Step 1: Creating a new variable that is the product of each user's corr and rating.

	Step 2: Creating a new dataframe containing the movie id and the average value of the weighted ratings 
	of all users of each movie.

	Step 3: Sort weighted ratings according to a condition.


*Item Based Recommendation*

Task 1: Make an item-based suggestion based on the most recent and highest rated movie the user has watched.


	Step 1: Getting the id of the movie with the most recent score from the movies that the selected user 
	gave 5 points.

	Step 2: Filtering the user_movie_df dataframe created in the User based recommendation section according 
	to the selected movie id.

	Step 3: Using the filtered dataframe, finding the correlation of the selected movie with the other 
	movies and ranking them.

	Step 4: Giving the first 5 movies as suggestions except the selected movie itself.

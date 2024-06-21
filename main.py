import pandas as pd
import matplotlib.pyplot as plt

#  * 1. Load the CSV file and store as netflix_df.
netflix_df = pd.read_csv('netflix_data.csv')
#  * 2. Filter the data to remove TV shows and store as netflix_subset.
netflix_subset = netflix_df[netflix_df['type'] == 'TV Show']
netflix_subset.to_csv('netflix_subset.csv')
#print(netflix_subset)
#  * 3. Investigate and subset the Netflix movie data, keeping only the columns "title", "country", "genre",
#  *    "release_year", "duration", and saving this into a new DataFrame called netflix_movies.
netflix_movies = netflix_df[['title', 'country', 'genre', 'release_year', 'duration']]
netflix_movies.to_csv('netflix_movies.csv')
#print(netflix_movies)

#  * 4. Filter netflix_movies to find the movies that are strictly shorter than 60 minutes, saving the resulting
#  *    DataFrame as short_movies; inspect the result to find possible contributing factors.
short_movies = netflix_movies[netflix_movies['duration'] < 60]
short_movies.to_csv('short_movies.csv')
#print(short_movies)
#  * 5. Using a for loop and if/elif statements, iterate through the rows of netflix_movies and assign colors of
#  *    your choice to four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else).
#  *    Save the results in a colors list.
colors = []
for index, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')
#  * 6. Initialize a matplotlib figure object called fig and create a scatter plot for movie duration by release year
#  *    using the colors list to color the points and using the labels "Release year" for the x-axis, "Duration (min)"
#  *    for the y-axis, and the title "Movie Duration by Year of Release".
fig = plt.figure()
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release Black: Other, Red: Children, Blue: Documentaries, Green: Stand-Up')

plt.show()

#  * 7. After inspecting the plot, answer the question "Are we certain that movies are getting shorter?" by assigning
#  *    either "yes" or "no" to the variable answer.
answer = 'no'
print(answer)
#  * 8. Save the figure as a PNG file called "movie_duration_years.png".
fig.savefig('movie_duration_years.png')

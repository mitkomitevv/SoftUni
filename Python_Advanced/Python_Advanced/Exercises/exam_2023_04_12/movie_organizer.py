def movie_organizer(*args):
    movies = {}

    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    # for genre in movies:
    #     movies[genre].sort()
    #
    #
    # sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))
    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0], sorted(x[1])))

    # result = []
    # for genre, movie in sorted_movies:
    #     movie_list = f"{genre} - {len(movie)}\n* " + "\n* ".join(movie)
    #     result.append(movie_list)
    #
    # return '\n'.join(result)

    return '\n'.join([f"{genre} - {len(movie)}\n* " + "\n* ".join(movie) for genre, movie in sorted_movies])


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

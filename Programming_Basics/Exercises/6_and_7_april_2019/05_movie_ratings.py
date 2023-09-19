import sys

number_of_movies = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
total_rating = 0
average_rating = 0

for _ in range(number_of_movies):
    movie_name = input()
    rating = float(input())

    total_rating += rating
    if rating > max_rating:
        max_rating = rating
        max_rating_movie = movie_name
    if rating < min_rating:
        min_rating = rating
        min_rating_movie = movie_name

average_rating += total_rating / number_of_movies

print(f'{max_rating_movie} is with highest rating: {max_rating:.1f}')
print(f'{min_rating_movie} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')

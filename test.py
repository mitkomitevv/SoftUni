import sys

num_movies = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
total_rating = 0

for _ in range(num_movies):
    movie_name = input()
    rating = float(input())

    total_rating += rating
    if rating > highest_rating:
        highest_rating = rating
        highest_rated_movie = movie_name
    if rating < lowest_rating:
        lowest_rating = rating
        lowest_rated_movie = movie_name

average_rating = total_rating / num_movies

print(f"{highest_rated_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rated_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

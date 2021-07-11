# importing modules
from turtle import Turtle, Screen
import random
from move_gen import User_interface

# creating objects
screen = Screen()  # object for the screen
user = User_interface()  # object for turtle

# file handling
striped_movie_list = []
with open("movies.txt") as movies_file:  # opening the file as movies_file
    movies_list = movies_file.readlines()  # readlines function makes list contains every line of the file


# Function for random select the movie and passing the movie to user.movie_display
def movie_display():
    with open("selected_movies.txt") as re_movies:
        ref_movie = re_movies.read()

    movie = random.choice(movies_list)
    if movie == ref_movie:
        movie = random.choice(movies_list)
    with open("selected_movies.txt", mode="a") as fi_movies:
        fi_movies.write(movie)
    user.movie_display(movie)


user.int_display()
screen.listen()
screen.onkeypress(movie_display, "m")
screen.exitonclick()

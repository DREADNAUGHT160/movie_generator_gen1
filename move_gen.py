import random
import turtle
from turtle import Turtle
import time

POSITION_OF_MESSAGE = (-270, 0)
turtle.colormode(255)
color = [(187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242),
         (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214),
         (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50),
         (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111),
         (162, 29, 27), (234, 171, 164), (162, 212, 176)]


class User_interface(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION_OF_MESSAGE)

    def int_display(self):

        self.write("Press m for Generating movie", font=("Arial", 30, "normal"))

    def movie_display(self, movie):
        self.clear()
        self.goto(POSITION_OF_MESSAGE)
        for i in range(1, 5):
            self.color(random.choice(color))
            self.write(f"searching...", align="left", font=("Arial", 30, "normal"))
            time.sleep(0.1)
            self.write(f"searching......", align="left", font=("Arial", 30, "normal"))
            time.sleep(0.1)
            self.write(f"searching........", align="left", font=("Arial", 30, "normal"))
            time.sleep(0.1)
            self.write(f"searching..........", align="left", font=("Arial", 30, "normal"))
            time.sleep(0.1)
            self.write(f"searching............", align="left", font=("Arial", 30, "normal"))

            self.clear()
        self.color("red")
        self.write(f"Movie: {movie} \nENJOY THE MOVIE", font=("Arial", 30, "normal"))
        self.goto(-270, -50)
        self.color("black")
        self.write("Press m for Generating movie", font=("Arial", 10, "normal"))

    def text_writer(self, text, x=None, y=None):
        self.goto(x, y)
        self.clear()
        self.write(f"{text}")

import turtle
from turtle import Screen
import random

caspar = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)

    return r, g, b


# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
turtle.speed("fastest")


def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        caspar.color(random_color())
        caspar.circle(100)
        caspar.setheading(caspar.heading() + size_gap)

draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()

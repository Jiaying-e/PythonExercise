import turtle
import random


# caspar.shape("turtle")


# def draw_square():
# square.forward(100)
# square.left(90)
# square.forward(100)
# square.left(90)
# square.forward(100)
# square.left(90)
# square.forward(100)
# for _ in range(4):
#     caspar.forward(100)
#     caspar.left(90)

# TODO Drawing a dashed line
# for i in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# TODO Drawing different shapes with random color
caspar = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)

    return r, g, b
# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


direction = [0, 90, 180, 270]
turtle.pensize(50)
turtle.speed(9)


# def draw_shape(number_sides):
#     angle = 360 / number_sides
#     for _ in range(number_sides):
#         caspar.forward(100)
#         caspar.right(angle)
#
#
# for sides in range(3, 11):
#     caspar.color(random.choice(colors))
#     draw_shape(sides)

for _ in range(200):
    caspar.color(random_color())
    caspar.forward(30)
    caspar.setheading(random.choice(direction))


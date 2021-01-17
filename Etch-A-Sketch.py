from turtle import Turtle, Screen

caspar = Turtle()
screen = Screen()


def move_forwards():
    caspar.forward(100)


def move_backwards():
    caspar.backward(100)


def turn_left():
    caspar.left(10)


def turn_right():
    caspar.right(10)


def clear():
    caspar.clear()
    caspar.penup()
    caspar.home()
    caspar.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()




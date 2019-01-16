import turtle
import time
from main import convert
import sys


def main():
    msg = "Hello world!"

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])

    dots = convert(msg)

    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    window = turtle.Screen()
    window.bgcolor("#000000")
    myPen.pensize(2)
    myPen.color("#FF00FF")

    dx = -500
    dy = 150

    for dot in dots:
        x, y, z = dot
        if z == 0:
            myPen.pendown()
            myPen.goto(x + dx, y + dy)
        else:
            myPen.penup()
            myPen.goto(x + dx, y + dy)


main()
time.sleep(2)

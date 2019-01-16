# -*- coding: utf-8 -*-
import turtle
import time
from main import convert
import sys


def main():
    msgs = ["Hello world!", u"Russian: Привет мир", "subscribe!"]

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        msgs = [msg]

    dots = convert(msgs)

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

if __name__ == '__main__':
    main()
    time.sleep(2)

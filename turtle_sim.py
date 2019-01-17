# -*- coding: utf-8 -*-
import turtle
import time
from main import convert
import sys


def main():
    # msgs = ["Hello world!", u"Russian: Привет мир", "subscribe!"]
    # msgs = [u"абвгд",u"ежзик",u"лмноп",u"рстуф",u"цчшщъ",u"ыьэюя",u".,!-й"]
    msgs = [u"Я был бы несчастливейшим из людей,",
            u"ежели бы я не нашел цели для моей",
            u"жизни - цели общей и полезной.",
            u"Теперь же жизнь моя будет вся",
            u"стремлением деятельным и постоянным",
            u"к этой одной цели."]

    dx = -300
    dy = 200

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        msgs = [msg]

    dots = convert(msgs, fontx=15, fonty=15)

    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    window = turtle.Screen()
    window.bgcolor("#000000")
    myPen.pensize(2)
    myPen.color("#FF00FF")

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
    time.sleep(5)

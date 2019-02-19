# -*- coding: utf-8 -*-
import turtle
import time
from main import convert, transform
import math
import sys


def main():
    #msgs = ["Hello world!", u"Russian: Привет мир", "subscribe!"]
    #msgs = [u"абвгд",u"ежзик",u"лмноп",u"рстуф",u"цчшщъ",u"ыьэюя",u".,!-й"]
            
    msgs = ["abcdef",
            "ghijkl",
            "mnopqr",
            "stuvwx",
            "yz"]

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        msgs = [msg]

    dots = convert(msgs,fontx=15,fonty=15)
    dots = transform(dots,[-200,100,0],[0,0,math.pi/3])

    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    window = turtle.Screen()
    window.bgcolor("#000000")
    myPen.pensize(2)
    myPen.color("#FF00FF")
    
    for dot in dots:
        x, y, z, a,b,c = dot        
        if z == 0:
            myPen.pendown()
        else:
            myPen.penup()
        myPen.goto(x,y)
            
if __name__ == '__main__':
    main()
    time.sleep(3)

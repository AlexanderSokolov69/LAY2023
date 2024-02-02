#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done
from math import sin, cos, radians


color1, color2, a = [int(d) if d.isnumeric() else d for d in input().split()]
arrow = Turtle()
arrow.speed(0)
arrow.pensize(6)
arrow.color(color1, color2)
arrow.pu()
for start_x in range(-2 * a, 2 * a + 1, 2 * a):
    t = 0
    x = start_x + 2 * a * cos(radians(t)) + a * cos(radians(2 * t))
    y = 2 * a * sin(radians(t)) + a * sin(radians(2 * t))
    arrow.goto(x, y)
    arrow.begin_fill()
    arrow.pd()
    for t in range(360):
        x = start_x + 2 * a * cos(radians(t)) + a * cos(radians(2 * t))
        y = 2 * a * sin(radians(t)) - a * sin(radians(2 * t))
        arrow.goto(x, y)
    arrow.end_fill()
    arrow.pu()
done()

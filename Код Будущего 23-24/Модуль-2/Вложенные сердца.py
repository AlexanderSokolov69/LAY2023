#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import cos, sin, radians


n, a0, step, *color = [int(x) for x in input().split()]
turtle.colormode(255)
# turtle.speed(0)
toms = [[turtle.Turtle(), a0 + step * (n - i - 1)] for i in range(n)]
for i in range(n):
    toms[i][0].color((color[0] - i * step,
                      color[1] - i * step,
                      color[2] - i * step,)
                     )
    toms[i][0].ht()
    toms[i][0].pu()
    toms[i][0].begin_fill()
for t in range(360):
    for i in range(n):
        a = toms[i][1]
        x = 2 * a * sin(radians(t)) - a * sin(2 * radians(t))
        y = 2 * a * cos(radians(t)) - a * cos(2 * radians(t))
        toms[i][0].goto(x, y)
        toms[i][0].pd()
for i in range(n):
    toms[i][0].end_fill()

turtle.done()

#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import cos, sin, radians


colors = input().split()
a0, *d = [int(x) for x in input().split()]
turtle.colormode(255)
turtle.tracer(0)
n = len(colors)
step = -5
m = 10
toms = [[turtle.Turtle(), a0 + step * i, d[i]] for i in range(n)]
for i in range(n):
    toms[i][0].color(colors[i])
    toms[i][0].pu()
    x = toms[i][1] * (m - 1) + toms[i][2]
    toms[i][0].goto(x, 0)
    toms[i][0].begin_fill()
for t in range(360):
    for i in range(n):
        a = toms[i][1]
        d = toms[i][2]
        x = a * (m - 1) * cos(radians(t)) + d * cos(radians(m * t - t))
        y = a * (m - 1) * sin(radians(t)) - d * sin(radians(m * t - t))
        toms[i][0].goto(x, y)
        toms[i][0].pd()
for i in range(n):
    toms[i][0].end_fill()
    toms[i][0].ht()
turtle.update()
turtle.done()

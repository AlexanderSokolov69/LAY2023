#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import radians, sin, cos, pi, gcd


colors = ['plum', 'crimson', 'orange', 'seagreen', 'blue']
A, B = [int(input()) for x in range(2)]
# turtle.tracer(0)
lissajous = turtle.Turtle()
lissajous.pensize(3)
n = 360
# A, B = -200, 200
a, b = 5, 5
phi = 0
i = 0
while phi <= pi / 2:
    lissajous.pu()
    lissajous.color(colors[i])
    k = gcd(a, b)
    for teta in range(n // k + 1):
        x = A * sin(a * radians(teta) + phi)
        y = B * sin(b * radians(teta))
        lissajous.goto(x, y)
        lissajous.pd()
    i += 1
    phi += pi / 8
lissajous.ht()
# turtle.update()
turtle.done()



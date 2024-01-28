#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import radians, sin, cos, pi, gcd


colors = ['violet', 'crimson', 'orangered', 'orange', 'yellow']
A, B = [int(input()) for x in range(2)]
# turtle.tracer(0)
lissajous = turtle.Turtle()
lissajous.pensize(3)
n = 360
# A, B = -200, 200
a, b = 2, 10
phi = 0

for a in range(2, 11, 2):
    lissajous.pu()
    lissajous.color(colors[a // 2 - 1])
    k = gcd(a, b)
    for teta in range(n // k + 1):
        x = A * cos(a * radians(teta) + phi)
        y = B * sin(b * radians(teta))
        lissajous.goto(x, y)
        lissajous.pd()
lissajous.ht()
# turtle.update()
turtle.done()


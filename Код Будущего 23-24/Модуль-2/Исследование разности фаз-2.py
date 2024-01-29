#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import radians, sin, pi, gcd


colors = ['plum', 'orchid', 'crimson', 'orange', 'seagreen', 'teal', 'blue']
A, B = [int(input()) for x in range(2)]
screen = turtle.Screen()
lissajous = turtle.Turtle()
lissajous.pensize(3)
lissajous.ht()
lissajous.speed(0)
n = 360
a, b = 1, 2
k = gcd(a, b)
i = 0
for i in range(len(colors)):
    lissajous.pu()
    lissajous.color(colors[i])
    phi = i * pi / 7
    for teta in range(n // k + 1):
        x = A * sin(a * radians(teta) + phi)
        y = B * sin(b * radians(teta))
        lissajous.goto(x, y)
        lissajous.pd()
lissajous.ht()
turtle.done()

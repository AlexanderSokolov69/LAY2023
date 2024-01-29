#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import cos, sin, radians


p, q = input().split()
colors = input().split()
m = int(p) / int(q)
a = 60
dot = 10
step = 10
turtle.tracer(0)
turtle.ht()
tom = turtle.Turtle()
tom.ht()
tom.pu()
tom.color(colors[0])
tom2 = turtle.Turtle()
tom2.ht()
tom2.pu()
tom2.color(colors[1])
x = m * a
y = 0
tom.goto(x, y)
tom2.goto(x, y)
tom2.left(90)
tom.left(90)
tom.pd()
tom.circle(m * a)
tom.pu()
for t in range(1, 360 * 3, step):
    tom2.pd()
    tom2.circle(-a)
    tom2.pu()
    tom2.circle(m * a, step)
    x = a * (m + 1) * cos(radians(t)) - a * cos((m + 1) * radians(t))
    y = a * (m + 1) * sin(radians(t)) - a * sin((m + 1) * radians(t))
    tom.goto(round(x), round(y))
    tom.dot(step)
turtle.update()
turtle.done()

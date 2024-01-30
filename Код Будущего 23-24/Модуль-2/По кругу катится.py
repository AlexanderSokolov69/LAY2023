#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import cos, sin, radians


p, q = [int(x) for x in input().split()]
colors = input().split()
m = p / q
a = 60
dot = 10
step = 10
tom = turtle.Turtle()
tom.speed(0)
tom.pu()
tom.color(colors[0])
tom.goto(m * a, 0)
tom.lt(90)
tom.pd()
tom.circle(m * a)
tom.pu()

tom2 = turtle.Turtle()
tom2.speed(0)
tom2.pu()
tom2.color(colors[1])
tom2.goto(m * a, 0)
tom2.lt(90)
n = 360
for t in range(0, n * q + 1, step):
    x = a * (m + 1) * cos(radians(t)) - a * cos(radians(m * t + t))
    y = a * (m + 1) * sin(radians(t)) - a * sin(radians(m * t + t))
    tom.goto(round(x), round(y))
    tom.dot(step)
    tom2.circle(m * a, step)
    tom2.pd()
    tom2.circle(-a)
    tom2.pu()
tom.ht()
tom2.ht()
turtle.done()

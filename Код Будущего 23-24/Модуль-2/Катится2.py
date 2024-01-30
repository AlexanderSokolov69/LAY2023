#!/usr/bin/env python3
# coding:utf-8
from math import sin, cos, radians
from turtle import Turtle, done


p, k = [int(x) for x in input().split()]
colors = input().split()
a = 60
m = p / k
epik = Turtle()
epik.speed(0)
epik.color(colors[0])
epik.pu()
epik.goto(a * m, 0)
epik.lt(90)
epik.pd()
epik.circle(a * m)
epik.pu()

wheel = Turtle()
wheel.speed(0)
wheel.color(colors[1])
wheel.pu()
wheel.goto(a * m, 0)
wheel.lt(90)
i = 0
n = 360
for t in range(0, n * k + 1, 10):
    x = a * (m + 1) * cos(radians(t)) - a * cos(radians(m * t + t))
    y = a * (m + 1) * sin(radians(t)) - a * sin(radians(m * t + t))
    epik.goto(x, y)
    epik.dot(10)
    wheel.circle(m * a, 10)
    wheel.pd()
    wheel.circle(-a)
    wheel.pu()
epik.ht()
wheel.ht()
done()

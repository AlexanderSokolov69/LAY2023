#!/usr/bin/env python3
# coding:utf-8
import turtle


DOLPHIN = ((-14, -2), (-8, 2), (-2, 4), (4, 8), (2, 4), (14, 0), (20, 2),
           (18, 0), (20, -2), (14, 0), (2, -4), (4, -8), (-2, -4), (-14, -2))
color1, color2, contour, mul, radius, count = [int(x) if x.isnumeric() else x for x in input().split()]
screen = turtle.Screen()
screen.register_shape('dolphin', DOLPHIN)
tom = turtle.Turtle()
tom.shape('dolphin')
tom.shapesize(mul + 1)
tom.color(color1, color2)
tom.pensize(contour)
tom.pu()
tom.goto(0, -(radius - contour))

step = 360 / count
for i in range(count):
    tom.stamp()
    tom.circle(radius - contour, step)
turtle.done()

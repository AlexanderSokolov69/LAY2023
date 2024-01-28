#!/usr/bin/env python3
# coding:utf-8
import turtle


STAR = ((-10, 0), (-2, 2), (0, 10), (2, 2),
        (10, 0), (2, -2), (0, -10), (-2, -2))
color, mul = [int(x) if x.isnumeric() else x for x in input().split()]
coords = [int(x) for x in input().split()]
screen = turtle.Screen()
screen.register_shape("star", STAR)
tom = turtle.Turtle()
tom.pu()
tom.ht()
tom.color(color)
tom.shapesize(mul)
tom.shape('star')
for i in range(len(coords) // 2):
    print(i)
    tom.goto(coords[i * 2], coords[i * 2 + 1])
    tom.stamp()
turtle.done()

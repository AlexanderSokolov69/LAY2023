#!/usr/bin/env python3
# coding:utf-8
from turtle import done, addshape, Turtle


coords = []
while True:
    test = input()
    if test:
        x, y = [int(x) for x in test.split()]
        coords.append((x, y))
    else:
        break
addshape('berry.gif')
tom = Turtle()
tom.pu()
tom.ht()
tom.shape('berry.gif')
tom.speed(0)
for coord in coords:
    tom.goto(*coord)
    tom.stamp()
done()

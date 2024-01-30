#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done


color = input()
side = int(input())
n = int(input())
angle = 360 / n
step = n // 2
corners = []
star = Turtle()
star.speed(0)
star.color(color)
star.pensize(4)
star.pu()
star.goto(-side / 2, -side / 2)
for _ in range(n):
    corners.append(star.pos())
    star.fd(side)
    star.lt(angle)
i = 0
star.pd()
for _ in range(n):
    i = (i + step) % n
    star.goto(*corners[i])
star.ht()
done()

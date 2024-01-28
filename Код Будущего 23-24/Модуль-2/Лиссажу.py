#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import radians, sin, pi, gcd


color = input()
A, B, a, b = [int(input()) for x in range(4)]
turtle.tracer(0)
lissajous = turtle.Turtle()
lissajous.color(color)
lissajous.pensize(3)
n = 360
# A, B = -200, 200
# a, b = 1, 3
if abs(A) == A and abs(B) == B:
    phi = 0
else:
    phi = pi / 4
lissajous.pu()
k = gcd(a, b)
for teta in range(n // k + 1):
    # расчет координат
    x = A * sin(a * radians(teta) + phi)
    y = B * sin(b * radians(teta))
    # переход в точку
    lissajous.goto(x, y)
    # рисование
    lissajous.pd()
lissajous.ht()
lissajous.pu()
lissajous.goto(0, abs(B))
lissajous.write(f'a = {a}, b = {b}', align='center', font=('Times New Roman', 24, 'normal'))
turtle.update()
turtle.done()

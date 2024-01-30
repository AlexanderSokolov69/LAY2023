#!/usr/bin/env python3
# coding:utf-8
import turtle
import math


sun_color = input()
water_color = input()
iland_color = input()
palm_color = input()
list_color = input()

bob = turtle.Turtle()
bob.speed(0)
bob.penup()
bob.goto(-150, 0)
bob.color(sun_color)
bob.begin_fill()
bob.pendown()
for x in range(-150, 151, 5):
    y = (150 ** 2 - x ** 2) ** 0.5
    bob.goto(x, y)
bob.end_fill()
bob.penup()

bob.goto(-350, -300)
bob.color(water_color)
bob.begin_fill()
bob.pendown()
for x in range(-350, 351, 5):
    y = 10 * math.sin(0.144 * x) + 10
    bob.goto(x, y)
bob.goto(350, -300)
bob.end_fill()
bob.penup()

bob.goto(-100, -105)
bob.color(iland_color)
bob.begin_fill()
bob.pendown()
for x in range(-100, 201, 5):
    y = -0.0025 * (x - 50) ** 2 - 50
    bob.goto(x, y)
for x in range(200, -101, -5):
    y = 0.0005 * (x - 50) ** 2 - 118
    bob.goto(x, y)
bob.end_fill()
bob.penup()

bob.goto(-8, 206)
bob.color(palm_color)
bob.begin_fill()
bob.pendown()
for x in range(-8, 81):
    y = 80 * (80 - x) ** 0.3 - 100
    bob.goto(x, y)
for x in range(30, -9, -1):
    y = 50 * (30 - x) ** 0.5 - 100
    bob.goto(x, y)
bob.end_fill()
bob.penup()

bob.goto(-40, 138)
bob.color(list_color)
bob.begin_fill()
bob.pendown()
for x in range(-40, 21):
    y = 0.002 * (x + 8) ** 3 + 206
    bob.goto(x, y)
for x in range(20, -41, -1):
    y = 2.05 * x + 221
    bob.goto(x, y)
bob.end_fill()
bob.penup()
bob.goto(-52, 258)
bob.begin_fill()
bob.pendown()
for x in range(-52, -7):
    y = -0.0195 * (x + 60) ** 2 + 260
    bob.goto(x, y)
for x in range(-8, -53, -1):
    y = 0.02 * x ** 2 + 205
    bob.goto(x, y)
bob.end_fill()
bob.penup()
bob.ht()

turtle.done()

#!/usr/bin/env python3
# coding:utf-8
import turtle


radius = [int(input()) for _ in range(6)]
color = []
color.append(tuple(int(input()) for _ in range(3)))
names = ['SATURN', 'D', 'C', 'B', 'A', 'F']
for i in range(5):
    color.append((color[-1][0] - 20,
                 color[-1][1] - 20,
                 color[-1][2] - 20))
shift = [-380, -315]
screen = turtle.Screen()
# screen.screensize(600, 400)
screen.colormode(255)
screen.tracer(0)
writer = turtle.Turtle()
writer.ht()
writer.pu()
writer.color('white')
font = ('Pacifico', 36, 'normal')
for i in range(6):
    sat = turtle.Turtle()
    sat.ht()
    sat.pu()
    sat.color(*color[i])
    if i == 0:
        sat.goto(*shift)
        sat.begin_fill()
        sat.goto(shift[0] + radius[i], shift[1])
        sat.left(90)
        sat.circle(radius[i], 90)
        sat.end_fill()
        writer.goto(shift[0] + radius[0] // 2, shift[1])
    else:
        sat.goto(shift[0] + 10 + radius[i - 1], shift[1])
        sat.begin_fill()
        sat.pd()
        sat.left(90)
        sat.circle(radius[i - 1] + 10, 90)
        sat.right(90)
        sat.forward(radius[i] - radius[i - 1] - 10)
        sat.right(90)
        sat.circle(-radius[i], 90)
        sat.end_fill()
        writer.goto(shift[0] + radius[i] - (radius[i] - radius[i - 1] - 10) // 2, shift[1])
    writer.write(names[i], align='center', font=font)

screen.update()
turtle.done()

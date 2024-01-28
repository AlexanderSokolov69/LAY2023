#!/usr/bin/env python3
# coding:utf-8
import turtle


coord = [['ϵ'], ['δ'], ['γ'], ['α'], ['β']]
name = 'Κασσιόπη'
for i in range(5):
    coord[i] += [int(input())] + [int(input())]
square = [(-320, 240), (320, 240),
          (320, -240), (-320, -240)]
screen = turtle.Screen()
screen.tracer(0)
field = turtle.Turtle()
field.color("#191970")
field.ht()
field.pu()
field.goto(square[0])
field.pd()
field.begin_fill()
for i in range(4):
    field.goto(square[i])
field.end_fill()
field.pu()
field.goto(0, square[0][1])
field.write(name, align='center', font=('Comfortaa', 48, 'normal'))
dots = turtle.Turtle()
dots.color('#FF0')
dots.pu()
dots.ht()
dots.pensize(3)
letters = turtle.Turtle()
letters.ht()
letters.pu()
letters.color('white')
for i in range(5):
    dots.goto(*coord[i][1:])
    dots.dot(8)
    dots.pd()
    letters.goto(*coord[i][1:])
    letters.write(coord[i][0], align='center', font=('Comfortaa', 24, 'normal'))

screen.update()
turtle.done()

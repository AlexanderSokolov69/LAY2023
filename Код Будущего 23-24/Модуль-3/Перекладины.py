#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done, tracer, update


# def draw(pen, 0, start_point, length, pen_th, dot_size)
def draw(bob: Turtle, num_iter, point, length, pen_th, dot_size):
    bob.speed(0)
    bob.pu()
    bob.color(color)
    bob.ht()
    num_iter += 1
    if num_iter > glub:
        return
    bob.goto(*point)
    bob.pensize(pen_th)
    bob.seth(0)
    bob.pd()
    bob.fd(length // 2)
    x = bob.xcor()
    y = bob.ycor()
    bob.seth(90)
    bob.fd((length / coef) // 2)
    bob.dot(dot_size)

    draw(Turtle(), num_iter, (bob.xcor(), bob.ycor()), length // step_len,
         pen_th + step_th, dot_size + step_th)
    # ---------------
    bob.pu()
    bob.goto(x, y)
    bob.pd()
    bob.seth(270)
    bob.fd((length / coef) // 2)
    bob.dot(dot_size)
    draw(Turtle(), num_iter, (bob.xcor(), bob.ycor()), length // step_len,
         pen_th + step_th, dot_size + step_th)
    # ---------------
    bob.pu()
    bob.goto(*point)
    bob.seth(180)
    bob.pd()
    bob.fd(length // 2)
    x = bob.xcor()
    y = bob.ycor()
    bob.seth(90)
    bob.fd((length / coef) // 2)
    bob.dot(dot_size)
    draw(Turtle(), num_iter, (bob.xcor(), bob.ycor()), length // step_len,
         pen_th + step_th, dot_size + step_th)
    # ---------------
    bob.pu()
    bob.goto(x, y)
    bob.pd()
    bob.seth(-90)
    bob.fd((length / coef) // 2)
    bob.dot(dot_size)
    draw(Turtle(), num_iter, (bob.xcor(), bob.ycor()), length // step_len,
         pen_th + step_th, dot_size + step_th)
    # ---------------


color = 'limegreen' # input()
glub = 2  # int(input())
tracer(0)
start_point = (0, 0)
length = 300
pen_th = 10
dot_size = 20
coef = 1.618

step_th = -2
step_len = 2

# pen.speed(-1)
draw(Turtle(), -1, start_point, length, pen_th, dot_size)
update()
done()

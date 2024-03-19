#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import Turtle, done, bgpic, setup


def draw(bob: Turtle, num_iter, start_angle, point, length, pen_th):
    num_iter += 1
    if num_iter > glub:
        return
    bob.goto(*point)
    bob.pensize(pen_th)
    bob.seth(start_angle)
    bob.pd()
    bob.fd(length)
    x = bob.xcor()
    y = bob.ycor()
    length //= 2
    pen_th -= 1
    bob.pensize(pen_th)
    bob.lt(angle)
    bob.fd(length)
    draw(bob, num_iter, start_angle - angle, (x, y), length, pen_th)
    bob.pu()
    bob.goto(x, y)
    bob.seth(start_angle)
    bob.rt(angle)
    bob.pd()
    bob.fd(length)
    draw(bob, num_iter, start_angle + angle, (x, y), length, pen_th)


x, y = [int(x) for x in input().split()]
glub = int(input())
fon = 'fon4.png'
im = Image.open(fon)
size = w, h = im.size
del im
setup(w, h)
bgpic(fon)

start_point = (x, y)
length = 200
pen_th = 10
color = 'maroon'

step_th = -1
step_len = 2
angle = 45

pen = Turtle()
pen.pu()
pen.color(color)
pen.ht()
pen.speed(0)
draw(pen, 0, 90, start_point, length, pen_th)

done()

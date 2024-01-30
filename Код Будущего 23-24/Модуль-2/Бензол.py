#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done


w = int(input())
a_c = 2 * w // 4
a_h = 2 * w // 6
step = w // 4 + w // 6
tom = Turtle()
tom.speed(0)
angle = 360 // 6
tom.pu()
tom.pensize(2)
tom.lt(90)
tom2 = Turtle()
tom2.speed(0)
tom2.pu()
tom2.pensize(2)
tom2.lt(90)
tom2.fd(w)
tom2.lt(120)
tom2.pd()
for i in range(6):
    tom2.fd(w)
    tom2.lt(angle)
    tom.fd(w)
    tom.color('black')
    tom.pd()
    tom.fd(step)
    tom.pu()
    tom.color('red')
    tom.dot(a_h)
    tom.bk(step)
    tom.color('blue')
    tom.dot(a_c)
    tom.goto(0, 0)
    tom.lt(angle)
tom.ht()
tom2.ht()
done()
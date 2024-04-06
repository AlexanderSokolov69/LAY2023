#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done, tracer, update


def kox(bob: Turtle,size=100, step=0):
    l_sys = "F-F+F-F"
    for el in l_sys:
        if el == 'F':
            if step > 0:
                kox(bob, size // 3, step - 1)
            else:
                bob.fd(size)
                break
        if el == '-':
            bob.left(60)
        if el == '+':
            bob.right(120)


with open('koch.txt', 'r') as f:
    data = list(map(str.strip, f.readlines()))
step = int(data[1])
size = 500
bob = Turtle()
tracer(0)
bob.color(data[0])
bob.ht()
bob.pu()
bob.goto(-250, 150)
bob.pd()
bob.speed(0)
for n in range(3):
    kox(bob, size=size, step=step)
    bob.right(120)
update()
done()

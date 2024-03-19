#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import Turtle, done, bgpic, setup


color = input()
n = int(input())
im = Image.open('sky.png')
size = w, h = im.size
del im
setup(w, h)
bgpic('sky.png')
tom = Turtle()
tom.ht()
tom.speed(0)
tom.color(color)
for i in range(n):
    tom.pensize((i + 1) // 2)
    tom.fd(i + 1)
    tom.left(30)
done()

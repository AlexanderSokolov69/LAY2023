#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import done, Turtle, bgpic, setup, addshape


n = int(input())
fon = 'fon.png'
im = Image.open(fon)
size = width, height = im.size
del im
# setup(width, height)
bgpic(fon)
fur = 'fur.gif'
addshape(fur)
tom = Turtle()
tom.ht()
tom.pu()
tom.speed(0)
tom.shape(fur)
tom.goto(-300, 150)

for i in range(n):
    tom.stamp()
    tom.circle(-700, 15)
done()

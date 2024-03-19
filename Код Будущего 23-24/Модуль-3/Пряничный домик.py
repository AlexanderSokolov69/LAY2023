#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import setup, bgpic, addshape, Turtle, done


s = input().split()
cx, cy = int(s[0]), int(s[1])
s = input().split()
x, y = int(s[0]), int(s[1])
fon = 'fon.png'
house = 'house.gif'
im = Image.open(fon)
size = width, height = im.size
im = Image.open(house)
im = im.resize((cx, cy))
im.save('test.gif')
# setup(width, height, startx=0, starty=0)
bgpic(fon)
addshape('test.gif')
tom = Turtle()
tom.shape('test.gif')
tom.goto(x, y)
tom.stamp()
tom.ht()

done()

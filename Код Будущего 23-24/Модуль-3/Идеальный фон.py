#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import setup, bgpic, done, Screen


im = Image.open('fon1.png')
size = width, height = im.size
w, h = 768, 648
dx = (width - w) // 2
dy = (height - h) // 2
im = im.crop((dx, dy, w + dx, h + dy))
screen = Screen()
im.save('temp.png')
setup(w, h, startx=0, starty=0)
bgpic('temp.png')
done()

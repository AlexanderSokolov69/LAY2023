#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageDraw


colorn = (0, 0, 0)


def rcol(y):
    global colorn
    colorn = (y, 0, 0)


def gcol(y):
    global colorn
    colorn = (0, y, 0)


def bcol(y):
    global colorn
    colorn = (0, 0, y)


def gradient(color):
    global colorn
    if color[0] == 'R':
        col = rcol
    elif color[0] == 'G':
        col = gcol
    else:
        col = bcol
    im = Image.new("RGB", (512, 200))
    draw = ImageDraw.Draw(im)
    y = 0
    for i in range(1, 512, 2):
        draw.polygon(((i + 0, 1),
                      (i + 1, 1),
                      (i + 1, 200),
                      (i + 0, 200)),
                     colorn)
        y += 1
        col(y)
    im.save('res.png')


gradient('R')

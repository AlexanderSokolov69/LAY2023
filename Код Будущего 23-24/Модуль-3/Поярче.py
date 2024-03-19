#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


im = Image.open('picture.png')
pix = im.load()
w, h = im.size
n = int(input())
for x in range(w):
    for y in range(h):
        r, g, b = pix[x, y]
        pix[x, y] = max(0, r - n), max(0, g - n), max(0, b - n)
im.save('result.png')

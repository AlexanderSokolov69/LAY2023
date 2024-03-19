#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


im = Image.open('settlement.png')
pix = im.load()
w, h = im.size
for x in range(w):
    for y in range(h):
        r, g, b = pix[x, y]
        r = max(0, r - 15)
        g = max(0, g - 15)
        b = min(255, b + 15)
        pix[x, y] = r, g, b
im = im.transpose(Image.FLIP_TOP_BOTTOM)

im.save('technique.png')

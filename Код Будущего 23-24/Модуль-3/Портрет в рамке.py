#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


bord = int(input())
color = input()
im = Image.open('portrait.png')
w, h = im.size
pix = im.load()
im_out = Image.new('RGB', (w + bord * 2, h + bord * 2), color)
pix_out = im_out.load()
for x in range(w):
    for y in range(h):
        pix_out[x + bord, y + bord] = pix[x, y]
im_out.save('border.png')

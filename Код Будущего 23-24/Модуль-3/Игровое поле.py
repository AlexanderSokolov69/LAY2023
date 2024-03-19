#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import done, bgpic, setup


with open('map.txt', 'r') as f:
    data = f.readlines()
h = len(data)
w = len(data[0].strip())
im = Image.new('RGB', (100 * w, 100 * h))
pix = im.load()
pict = {'0': Image.open('grass.png').load(), '1': Image.open('wall.png').load()}
for y in range(h):
    for x in range(w):
        pic = pict[data[y][x]]
        for cx in range(100):
            for cy in range(100):
                pix[cx + x * 100, cy + y * 100] = pic[cx, cy]
im.save('temp.png')
setup(100 * w, 100 * h)
bgpic('temp.png')

done()

#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from turtle import done, bgpic, setup


im = Image.open('castle.png')
size = w, h = im.size
pix = im.load()

im_out = Image.new('RGB', size)
pix_out = im_out.load()

with open('puzzle.txt', 'r') as f:
    puzzle = list(map(int, f.readlines()))
for i in range(9):
    x, y = i % 3, i // 3
    x_out, y_out = puzzle[i] % 3, puzzle[i] // 3
    for row in range(h // 3):
        for col in range(w // 3):
            pix_out[col + x_out * (w // 3), row + y_out * (h // 3)] = pix[col + x * (w // 3), row + y * (h // 3)]
im_out.save('temp.png')

setup(w, h)
bgpic('temp.png')
done()

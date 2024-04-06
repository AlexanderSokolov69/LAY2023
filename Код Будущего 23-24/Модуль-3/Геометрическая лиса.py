#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageDraw


w = int(input())
im = Image.new('RGB', (12 * w, 14 * w), '#ffffff')
draw = ImageDraw.Draw(im)
cont_width = 2
orange = '#ffa000'
data = [
    ((0, 9 * w), (6 * w, 11 * w), (12 * w, 9 * w), (11 * w, 7 * w), (w, 7 * w)),
    ((w, 7 * w), (2 * w, 0), (3 * w, 3 * w)),
    ((w, 7 * w), (3 * w, 3 * w), (4.5 * w, 8.4 * w)),
    ((2 * w, 0), (3 * w, 3 * w), (6 * w, 3 * w)),
    ((4.5 * w, 8.4 * w), (3 * w, 3 * w), (9 * w, 3 * w), (7.5 * w, 8.4 * w), (6 * w, 9 * w)),
    ((6 * w, 3 * w), (10 * w, 0), (9 * w, 3 * w)),
    ((10 * w, 0), (11 * w, 7 * w), (9 * w, 3 * w)),
    ((7.5 * w, 8.4 * w), (9 * w, 3 * w), (11 * w, 7 * w))
]

for poly in data:
    draw.polygon(poly, orange, '#000000', cont_width)
draw.polygon(((w, 7 * w), (6 * w, 9 * w), (11 * w, 7 * w), (6 * w, 14 * w)),
             '#ffffff', '#000000', cont_width)
draw.polygon(((4.5 * w, 8.4 * w), (6 * w, 9 * w), (7.5 * w, 8.4 * w), (6 * w, 14 * w)),
             '#000000')

im.save('fox.png')

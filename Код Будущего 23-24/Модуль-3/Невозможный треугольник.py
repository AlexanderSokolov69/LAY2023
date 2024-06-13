#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageDraw


colors = ['ghostwhite', 'gainsboro', 'darkgray']
w = int(input())
im = Image.new('RGB', (18 * w, 19 * w), '#ffffff')
draw = ImageDraw.Draw(im)
cont_width = 2
cont_color = 'dimgray'
data = []
data.append(((0, w), (14 * w, 8 * w), (14 * w, 10 * w), (2 * w, 4 * w), (2 * w, 19 * w), (0, 18 * w)))
data.append(((0, w),(2 * w, 0), (18 * w, 8 * w), (4 * w, 16 * w), (3 * w, 14 * w), (14 * w, 8 * w)))
data.append(((2 * w, 4 * w),(4 * w, 5 * w), (4 * w, 16 * w), (18 * w, 8 * w), (18 * w, 10 * w), (2 * w, 19 * w)))
for i, points in enumerate(data):
    draw.polygon(points, colors[i], cont_color, cont_width)

im.save('triangle.png')

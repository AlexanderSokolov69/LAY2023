#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageDraw


N = int(input())
image = Image.new("RGB", (18 * N, 15 * N), 'white')
draw = ImageDraw.Draw(image)
draw.ellipse(((N, N), (int(6.5 * N), 7 * N)), outline='black', width=int(0.8 * N))
draw.ellipse(((int(11.5 * N), N), (int(17 * N), 7 * N)), outline='black', width=int(0.8 * N))
draw.ellipse(((2 * N, N), (16 * N, 14 * N)), fill='white', outline='black', width=int(0.5 * N))
draw.ellipse(((int(3.5 * N), 7 * N), (int(6.5 * N), 11 * N)), 'black')
draw.ellipse(((int(11.5 * N), 7 * N), (int(14.5 * N), 11 * N)), 'black')
draw.ellipse(((int(8 * N), int(9.5 * N)), (int(10 * N), int(10.5 * N))), 'black')

draw.ellipse(((int(4.5 * N), int(8 * N)), (int(5.5 * N), int(9 * N))), 'white')
draw.ellipse(((int(12.5 * N), int(8 * N)), (int(13.5 * N), int(9 * N))), 'white')

image.save('panda.png')

#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


im = Image.open('input.png')
pix = im.load()
w, h = im.size
color = tuple(int(x) for x in input().split())
im_out = Image.new('RGB', (w, h * 3))
pix_out = im_out.load()
for dy in range(3):
    for x in range(w):
        for y in range(h):
            r, g, b = pix[x, y]
            if r > 200 and g > 200 and b > 200:
                if dy == 0:
                    r, g, b = color
                elif dy == 1:
                    r, g, b = color[1], color[0], color[2]
                else:
                    r, g, b = 255, max(0, color[0] - 50), max(0, color[2] - 50)
            pix_out[x, y + h * dy] = r, g, b

im_out.save('tomato.png')
im_out.show()

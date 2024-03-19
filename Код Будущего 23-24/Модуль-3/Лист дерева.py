#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


im = Image.open('leave0.png')
pix = im.load()
size = width, height = im.size
n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]

im_out = Image.new('RGB', (width * (n + 1), height))
pix_out = im_out.load()

for c in range(n + 1):
    for x in range(width):
        for y in range(height):
            pix_out[x + width * c, y] = pix[x, y]
            if c < n:
                r, g, b = pix[x, y]
                if r < 250 or g < 250 or b < 250:
                    r, g, b = colors[c][0], colors[c][1], colors[c][2]
                    pix[x, y] = r, g, b

im_out.save('leaves.png')

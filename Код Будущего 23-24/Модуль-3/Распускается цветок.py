#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


n = int(input())
im = Image.open('flower.png')
pix = im.load()
size = width, height = im.size
im_out = Image.new('RGB', (width * (n + 1), height), '#FFFFFF')
pix_out = im_out.load()
w, h = width, height
for c in range(n + 1):
    im_out.paste(im, (width * (n - c) + (width - im.width) // 2,
                      (height - im.height) // 2))
    w = h = w // n * (n - 1)
    im = im.resize((w, h))
    pix = im.load()

im_out.save('flowers.png', 'PNG')

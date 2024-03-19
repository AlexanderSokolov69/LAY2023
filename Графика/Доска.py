#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageDraw


def board(num, size):
    im = Image.new("RGB", (num * size, num * size), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(0, num * size, size * 2):
        for j in range(0, num * size, size * 2):
            draw.polygon(((i, j),
                          (i + size, j),
                          (i + size, j + size),
                          (i, j + size)),
                         (0, 0, 0))
            draw.polygon(((i + size, j + size),
                          (i + size * 2, j + size),
                          (i + size * 2, j + size * 2),
                          (i + size, j + size * 2)),
                         (0, 0, 0))
    im.save('res.png')


board(5, 30)

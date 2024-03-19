#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


n = float(input())
pic2 = Image.open('dino.png')
pic1 = Image.open('bird.png')
size = pic1.size
arr1 = pic1.load()
arr2 = pic2.load()

pic = Image.new("RGB", size)
arr = pic.load()
for x in range(pic.width):
    for y in range(pic.height):
        r1, g1, b1 = arr1[x, y]
        r2, g2, b2 = arr2[x, y]
        r = int(0.8 * n * r1 + (1 - n) * r2)
        g = int(0.8 * n * g1 + (1 - n) * g2)
        b = int(0.8 * n * b1 + (1 - n) * b2)
        arr[x, y] = r, g, b
pic.save('origin.png')
pic.show()

#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


n = int(input())
im = Image.open('flower1.png')
im = im.resize((n, n))
im.save('icon.png')

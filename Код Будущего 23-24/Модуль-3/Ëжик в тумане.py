#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageFilter


dx = int(input())
res = Image.open('forest.png')
hed = Image.open('hedgehog.png')
hed = hed.resize((hed.width // 2, hed.height // 2))
res.paste(hed, (dx, res.height - hed.height))
res = res.filter(ImageFilter.BLUR)
res.save('hedgehog_in_fog.png')

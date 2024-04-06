#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageFilter


n = int(input())
im = Image.open('alena.png')
im_out = Image.new('RGB', (im.width, im.height * 2))
im_out.paste(im, (0, 0))
im = im.transpose(method=Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(radius=n))
im_out.paste(im, (0, im.height))
im_out.save('result.png')

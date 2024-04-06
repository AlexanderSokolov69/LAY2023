#!/usr/bin/env python3
# coding:utf-8
from PIL import Image


def makeanagliph(fname, shift):
    im = Image.open(fname)
    r, g, b = im.split()
    r_new = Image.new('L', im.size)
    r_new.paste(r, (shift, 0))
    im_out = Image.merge('RGB', [r_new, g, b])
    im_out.save('res.jpg')
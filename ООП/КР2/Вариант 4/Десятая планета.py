#!/usr/bin/env python3
# coding:utf-8
from PIL import Image, ImageOps


def persephone(name, *args, reflect=1):
    im = Image.open(name)
    out = ImageOps.mirror(im) if reflect == 1 else ImageOps.flip(im)
    x, y = out.size
    pix = out.load()
    for col in range(x):
        for row in range(y):
            r, g, b = pix[col, row]
            r -= r // 3
            g = min(255, g + g // 3)
            b = min(255, b + b // 3)
            pix[col, row] = r, g, b
    res = Image.new('RGB', (600, 600))
    for i in range(6):
        x = i % 3
        y = i // 3
        cut = out.crop((*args[i], args[i][0] + 200, args[i][1] + 300))
        res.paste(cut, (x * 200, y * 300))
    return res


persephone(
    'persephone.png',
    (300, 200), (300, 400),
    (600, 400), (400, 600),
    (100, 700), (700, 600),
    reflect=-1
).save('result.png')

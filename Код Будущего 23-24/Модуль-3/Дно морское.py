#!/usr/bin/env python3
# coding:utf-8
from PIL import Image
from json import load


im = Image.open('bottom.png')
pix = im.load()
with open('task.json', 'r') as f:
    data = load(f)
dx, dy = data['paste'][:2]
for x in range(data['crab'][0], data['crab'][2] + 1):
    for y in range(data['crab'][1], data['crab'][3] + 1):
        pix[dx + x - data['crab'][0], dy + y - data['crab'][1]] = pix[x, y]

dx, dy = data['paste'][2:]
for x in range(data['bubble'][0], data['bubble'][2] + 1):
    for y in range(data['bubble'][1], data['bubble'][3] + 1):
        pix[dx + x - data['bubble'][0], dy + y - data['bubble'][1]] = pix[x, y]

im.save('result.png')

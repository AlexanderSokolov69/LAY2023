#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done, tracer, update
import json


tracer(0)
with open("points.json", 'r', encoding='utf8') as f:
    spis = json.load(f)
colors = ['coral', 'gold', 'red', 'pink', 'salmon']
ITER = 100
data = []
for i in range(len(spis)):
    data.append(Turtle())
    data[-1].ht()
    data[-1].speed(0)
    data[-1].color(colors[i])
    data[-1].pu()
    data[-1].goto(*spis[i])
for n in range(ITER):
    for t in data:
        t.pu()
        t.forward(n)
        t.left(160)
        t.pd()
        t.circle(ITER)
update()
done()

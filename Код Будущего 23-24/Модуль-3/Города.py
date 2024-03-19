#!/usr/bin/env python3
# coding:utf-8
import json


with open('names.txt', 'r', encoding='utf-8') as f:
    data = [x.strip() for x in f.readlines()]
spis = {}
for city in data:
    b = city[0]
    temp = spis.get(b, [])
    temp.append(city)
    spis[b] = sorted(temp)
with open('cities.json', 'w', encoding='utf-8') as f:
    json.dump(spis, f, ensure_ascii=False, indent=4)

#!/usr/bin/env python3
# coding:utf-8
import json


with open('question.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
cols = len(data[0])
rows = len(data)

data[rows // 2][cols // 2] = 0
itog = 0
for x in range(rows):
    itog += sum(data[x])
data[rows // 2][cols // 2] = itog
with open('response.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

#!/usr/bin/env python3
# coding:utf-8
import json


with open('names.json', 'r', encoding='utf-8') as f:
    spis = json.load(f)
out = {}
for i, data in enumerate(spis):
    rec = {}
    sur, name, age = data.split()
    rec['surname'] = sur
    rec['name'] = name
    rec['age'] = int(age)
    out[str(i + 1)] = rec
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=4)

#!/usr/bin/env python3
# coding:utf-8
import json


with open('factory.txt', 'r', encoding='utf-8') as f:
    data = [s.strip().split('\t') for s in f.readlines()]
out = {}
for el in data:
    out[el[0]] = {'cost': int(el[1])}
    out[el[0]]['dependencies'] = []
    if len(el) > 2:
        for dep in el[2].split(', '):
            out[el[0]]['dependencies'].append(dep)
with open('processes.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=4)

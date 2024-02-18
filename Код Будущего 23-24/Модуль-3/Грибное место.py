#!/usr/bin/env python3
# coding:utf-8
itog = {}
with open("mushroom_place.txt", 'r') as f:
    sp = list(map(str.strip, f.readlines()))
    for i in range(0, len(sp), 2):
        itog[sp[i]] = itog.get(sp[i], 0) + int(sp[i + 1])
print(itog)

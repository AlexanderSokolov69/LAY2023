#!/usr/bin/env python3
# coding:utf-8
colors = {}
for i in range(int(input())):
    data = input().split()
    for color in data:
        colors[color] = colors.get(color, 0) + 1
print(colors)

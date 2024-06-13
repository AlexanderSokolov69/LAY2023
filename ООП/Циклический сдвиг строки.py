#!/usr/bin/env python3
# coding:utf-8
from sys import stdin


shift = int(input())
data = map(str.strip, stdin)
for stroka in data:
    out = ''
    for x in range(len(stroka)):
        out += stroka[(x + shift) % len(stroka)]
    print(out)

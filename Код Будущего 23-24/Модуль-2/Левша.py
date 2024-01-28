#!/usr/bin/env python3
# coding:utf-8
import turtle


line = input().split()
i = 0
out = ''
while i < len(line):
    out += line[i]
    i += 1
    if i < len(line):
        if i % 6 == 0:
            out += '; '
        else:
            out += ', '
print(out)

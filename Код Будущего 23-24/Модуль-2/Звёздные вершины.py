#!/usr/bin/env python3
# coding:utf-8
n = int(input())
step = n // 2
out = [0]
i = 0
for _ in range(n):
    i = (i + step) % n
    out.append(i)
print(out)

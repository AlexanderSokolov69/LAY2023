#!/usr/bin/env python3
# coding:utf-8
n = 12040601001
p = 1
for i in str(n):
    x = int(i)
    if x != 0:
        p *= x
print(p)

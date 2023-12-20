#!/usr/bin/env python3
# coding:utf-8
sp = []
for n in range(int(input())):
    w1 = [int(w) for w in input().split(' . ')]
    sred = sum(w1) / len(w1)
    w1 += [int(w) for w in input().split(' . ')]
    print(n + 1, 'wave pair:', '_'.join([str(x) for x in set(w1) if x >= sred]))

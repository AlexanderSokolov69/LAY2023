#!/usr/bin/env python3
# coding:utf-8
def mul(sp):
    res = 1
    for ch in sp:
        res *= ch
    return res


n = int(input())
cnt = 0
for i in range(0, n + 1, 2):
    s = [int(s) for s in str(i)]
    if i < 10 or s[-1] != 2:
        continue
    if sum(s) < mul(s):
        cnt += 1
print(cnt)

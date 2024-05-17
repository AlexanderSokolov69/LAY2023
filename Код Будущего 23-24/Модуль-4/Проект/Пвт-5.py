#!/usr/bin/env python3
# coding:utf-8
s = "Lorem ipsum dolor sit amet consectetur adipiscing elit".split()
res = []
for i in range(len(s)):
    if len(s[i]) % 5 == 0:
        res.append(s[i])
print(len(res))

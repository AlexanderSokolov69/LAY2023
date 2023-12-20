#!/usr/bin/env python3
# coding:utf-8
mount = {}
for i in range(int(input())):
    sp = [s for s in input().lower() if 'a' <= s <= 'z']
    for test in set(sp):
        if sp.count(test) > 1:
            mount[i] = mount.get(i, "") + test
print(mount)

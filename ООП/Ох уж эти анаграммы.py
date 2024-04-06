#!/usr/bin/env python3
# coding:utf-8
data = {}
for _ in range(int(input())):
    word = input().lower()
    if len(word) > 1:
        key = ''.join(sorted(word))
        data.setdefault(key, set()).add(word)
print(*sorted([' '.join(sorted(value)) for value in data.values() if len(value) > 1]), sep='\n')

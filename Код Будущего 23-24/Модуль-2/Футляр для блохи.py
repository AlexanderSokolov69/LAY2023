#!/usr/bin/env python3
# coding:utf-8
line = input().split()
out = []
for i in range(len(line) // 2):
    out.append(f"({'-'.join(line[i * 2 + 1].split(line[i * 2]))})")
print(', '.join(out))

#!/usr/bin/env python3
# coding:utf-8
n = int(input())
print('{', end='')
for i in range(n):
    s = input()
    if i > 0:
        print(' ', end='')
    print(f"'{s}': '{''.join(sorted(set(s.lower())))}'", end='')
    if i < n - 1:
        print(',')
    else:
        print('}')
"""
8
Amphitrite
Dionysus
Triton
Asclepius
Uranus
Hades
Hephaestus
Hecate
"""
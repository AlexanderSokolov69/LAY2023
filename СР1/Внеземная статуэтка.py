#!/usr/bin/env python3
# coding:utf-8
import sys


monster = input().lower()
lines = [
    s for s in map(str.strip, sys.stdin)
    if any(map(
        lambda x: len(monster) < len(x) and monster == x[:len(monster)].lower(),
        s.split()
    ))
]
print(*lines, sep='\n')

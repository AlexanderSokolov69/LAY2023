#!/usr/bin/env python3
# coding:utf-8
print(*[sum(
    [(ord(x) if 'a' <= x <= 'z' else ord('a')) - ord('a') for x in list(s)]
) for s in input().lower().split()])

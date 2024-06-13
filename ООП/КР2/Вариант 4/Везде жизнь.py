#!/usr/bin/env python3
# coding:utf-8
from sys import stdin

words = []
[words.extend(word) for word in list(map(str.split, stdin))]
print(*set(el for el in words if len(el) != len(set(el.upper()))), sep='\n')

#!/usr/bin/env python3
# coding:utf-8
with open('hidden.txt', 'r') as f:
    data = sorted([s.strip()[1::2].capitalize() + '\n' for s in f.readlines()], reverse=True)
with open('opened.txt', 'w') as f:
    f.writelines(data)

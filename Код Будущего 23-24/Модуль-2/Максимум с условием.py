#!/usr/bin/env python3
# coding:utf-8
print(max([len(x) for x in input().split('Y') if x.count('E') >= 3]))

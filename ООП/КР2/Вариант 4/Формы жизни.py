#!/usr/bin/env python3
# coding:utf-8
def alive(*args, evolution=5):
    res = {}
    for el in args:
        n = str(len(el) % evolution)
        res[n] = sorted(res.get(n, []) + [el], reverse=True)
    return res

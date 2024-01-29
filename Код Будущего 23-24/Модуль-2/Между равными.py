#!/usr/bin/env python3
# coding:utf-8
line = input()
l_ind = 0
r_ind = len(line) - 1
result = {}
while l_ind < r_ind:
    test = line[l_ind + 1:].rfind(line[l_ind])
    if test >= 0:
        if not result.get(test):
            result[test] = (l_ind, test)
    l_ind += 1
    if result and r_ind - l_ind == 2:
        print(result)
        key = max(result.keys())
        l_ind = result[key][0]
        test = result[key][1]
        line = line[l_ind + 1: l_ind + test + 1: 1]
        print(line)
        l_ind = 0
        r_ind = len(line) - 1
        result.clear()


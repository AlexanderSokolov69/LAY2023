#!/usr/bin/env python3
# coding:utf-8
# 83 ? 20  *  1  *  14 ? 5
with open('numbers.txt', 'r') as f:
    data = [s.strip() for s in f.readlines()]
count = 0
for test in data:
    ok = True
    if test[:2] != '83':
        ok = False
    if test[3:5] != '20':
        ok = False
    if '1' not in test[5: -4]:
        ok = False
    if test[-4: -2] != '14':
        ok = False
    if test[-1:] != '5':
        ok = False
    if ok:
        count += 1
with open('answer.txt', 'w') as f:
    f.write(str(count))

#!/usr/bin/env python3
# coding:utf-8
start = int(input())
stop = int(input())
for n in range(start, stop):
    summa = 0
    ch = n
    while ch > 0:
        summa += ch % 10
        ch //= 10
    test = summa
    while test < stop:
        if test == n:
            print(n)
            break
        else:
            if test == 1:
                break
            else:
                test *= summa

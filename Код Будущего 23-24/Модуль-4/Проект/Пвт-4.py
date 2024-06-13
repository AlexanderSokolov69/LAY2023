#!/usr/bin/env python3
# coding:utf-8
n = 108556453701
m = 15
while n != 0:
    if n % 5 == 0:
        m += 1
    n //= 10
print(m)

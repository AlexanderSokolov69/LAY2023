#!/usr/bin/env python3
# coding:utf-8
sp = []
while True:
    n = input()
    if n == "GRAVITY":
        break
    elif int(n) > 1000 and int(n) % 2 != 0:
        sp.append(int(n))
print(sum(sp) / len(sp))

#!/usr/bin/env python3
# coding:utf-8
data = []
itog = 0
size = int(input())
for row in range(size):
    data.append(list(map(int, input().split(', '))))
    itog += data[-1][row] + data[-1][size - row - 1]
    data[-1][row], data[-1][size - row - 1] = data[-1][size - row - 1], data[-1][row]
    print(*data[-1])
print(itog)

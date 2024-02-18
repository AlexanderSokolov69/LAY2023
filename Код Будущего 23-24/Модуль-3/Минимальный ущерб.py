#!/usr/bin/env python3
# coding:utf-8
def count(x, y, summa=0):
    cost = data[y][x] + summa
    if x + y > 0:
        if x > 0:
            count(x - 1, y, cost)
        if y > 0:
            count(x, y - 1, cost)
    else:
        itog.append(cost)
        return


itog = []
data = []
for row in range(int(input())):
    data.append(list(map(int, input().split())))

rows = len(data)
cols = len(data[0])
row = rows - 1
col = cols - 1

count(col, row)
print(min(itog))

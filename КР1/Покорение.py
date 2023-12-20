#!/usr/bin/env python3
# coding:utf-8
data = []
while (st := input()) != "":
    data.append([int(x) for x in st.split()])
interfering = set()
helping = set()
neutral = set()
chet = []
cnt = len(data)
for x in range(len(data[0])):
    res = 0
    for y in range(len(data)):
        res += data[y][x]
    chet.append(((res + 1) % 2, res / cnt))
data.append(chet)
for y in range(len(data) - 1):
    for x in range(len(data[0])):
        if data[y][x] > data[-1][x][1] and data[y][x] % 2 == data[-1][x][0]:
            interfering.add(data[y][x])
        sr = sum(data[y]) / len(data[y])
        if data[y][x] % 2 == 0 and data[y][x] < sr:
            helping.add(data[y][x])
        if data[y][x] % 2 != 0 and sr - sr / 2 <= data[y][x] < sr + sr / 2:
            neutral.add(data[y][x])

print(f"Interfering {'-'.join([str(n) for n in sorted(interfering, reverse=True)])};")
print(f"Helping {'-'.join([str(n) for n in sorted(helping, reverse=True)])};")
print(f"Neutral {'-'.join([str(n) for n in sorted(neutral, reverse=True)])}.")

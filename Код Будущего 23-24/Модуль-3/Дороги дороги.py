#!/usr/bin/env python3
# coding:utf-8
routes = []
while True:
    line = input().strip()
    if line:
        routes.append(line)
    else:
        break
points = sorted(set(''.join(routes)))
addr = {}
for i, l in enumerate(points):
    addr[l] = i
size = len(points)
data = [['0'] * size for _ in range(size)]
for y, x in routes:
    data[addr[y]][addr[x]] = '1'
print('  ' + ' '.join(list(points)))
for i in range(size):
    print(f'{points[i]} {" ".join(data[i])}')

#!/usr/bin/env python3
# coding:utf-8
result = {}
while True:
    data = input().strip()
    if data:
        name, summa = data.split(' - ')
        result[name] = result.get(name, 0) + int(summa.split()[0])
    else:
        break
out = [f"{line[0]}: {line[1]} руб." for line in sorted(result.items(),
                                                       key=lambda x: (x[1], x[0]),
                                                       reverse=True)]
print(*out, sep='\n')

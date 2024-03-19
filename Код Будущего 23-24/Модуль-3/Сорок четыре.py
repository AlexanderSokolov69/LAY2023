#!/usr/bin/env python3
# coding:utf-8
with open('numbers.txt', 'r') as f:
    data = [int(s.strip()) for s in f.readlines()]
    data11 = [x for x in data if x % 44 != 0 and (x % 11 == 0 or x % 2 == 0)]
    data44 = [x for x in data if x % 44 == 0]
count = 0
for i in range(len(data11)):
    for j in range(i + 1, len(data11)):
        if data11[i] != data11[j]:
            if (data11[i] * data11[j]) % 44 == 0:
                count += 1
print(count)
# print(data44, len(data) - 2)

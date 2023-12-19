#!/usr/bin/env python3
# coding:utf-8

test = {1: "A", 2: "B", 3: "C"}
k = test.keys()
v = test.values()

print(k)
print(v)

test[2] = "BB"
test[4] = "DDD"

print(*k)
print(*v)

for item in test.items():
    print(item)

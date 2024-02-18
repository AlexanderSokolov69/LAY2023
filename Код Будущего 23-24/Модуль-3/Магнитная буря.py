#!/usr/bin/env python3
# coding:utf-8
with open("magnetic.txt", 'r') as f:
    days = [line.split(":") for line in map(str.strip, f.readlines())]
for day in days:
    states = list(map(int, day[1].strip().split()))
    mid = sum(states) / len(states)
    count = 0
    for level in states:
        if level > mid:
            count += 1
        else:
            count = 0
        if count >= 3:
            print(day[0])
            break

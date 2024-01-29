#!/usr/bin/env python3
# coding:utf-8
line = input()
letters = set([x for x in line if 'a' <= x.lower() <= 'z'])
win = ['', 0]
for let in line:
    if let in letters:
        count = line.count(let)
        if count > win[1]:
            win[:] = [let, count]
out = []
for i in range(win[1]):
    if out:
        out.append(str(line.find(win[0], int(out[-1]) + 1)))
    else:
        out.append(str(line.find(win[0])))
print(', '.join(out))

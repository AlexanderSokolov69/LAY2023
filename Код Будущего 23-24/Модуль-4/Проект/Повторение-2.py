#!/usr/bin/env python3
# coding:utf-8
s = input()
n = int(input())
shifr = {'01': '1021102',
         '021': '1201'}
i = 0
out = ''
while True:
    if len(s) > i + 1:
        if s[i: i + 2] == '01':
            out += shifr['01']
            i += 2
        else:
            out += s[i]
            i += 1
    else:
        break
print(out)
out2 = ''
i = 0
while True:
    if len(out) > i + 1:
        if out[i: i + 3] == '021':
            out2 += shifr['021']
            i += 3
        else:
            out2 += out[i]
            i += 1
    else:
        break

print(out2)

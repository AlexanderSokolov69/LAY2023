#!/usr/bin/env python3
# coding:utf-8
alp = 'АБВГДЕËЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯА'
word = "АУТЕНТИФИКАЦИЯ"
res = ''
for w in word:
    res += chr(ord(w) + 1)
alp2 = ''
for i in range(len(alp)):
    alp2 += alp[(i + 1) % 33]

for w in word:
    i = alp.find(w)
    print(w, alp2[i])


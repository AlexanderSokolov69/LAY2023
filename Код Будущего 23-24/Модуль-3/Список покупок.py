#!/usr/bin/env python3
# coding:utf-8
magazine = {}
while True:
    line = input().strip()
    if line:
        key, name = line[: line.find(' ')], line[line.find(' ') + 1:]
        magazine[key] = name
    else:
        break

spisok = {}
while True:
    data = input().strip()
    if data:
        line = data.split('. ')
        key = magazine[line[0]]
        spisok[key] = sorted(spisok.get(key, []) + [line[1]])
    else:
        break
print(spisok)

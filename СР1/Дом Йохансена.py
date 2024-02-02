#!/usr/bin/env python3
# coding:utf-8
def knowledge(line, check="mate"):
    dop = []
    for i, word in enumerate(house):
        if len(set(check) & set(word)) > 1:
            dop.append(word)
            house[i] = line
    house[:] = dop + house


house = ['paws', 'tentacles', 'face', 'mud', 'head', 'appearance']
knowledge('horror', 'Cthulhu')
print(house)

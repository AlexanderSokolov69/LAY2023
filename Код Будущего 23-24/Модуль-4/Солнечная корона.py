#!/usr/bin/env python3
# coding:utf-8
def elements(data):
    res = []
    data = set(data)
    for e, nums in spectrum.items():
        if len(nums) == len(set(nums) & data):
            res.append(e)
    return res


spectrum = {'H': (410, 430, 486, 656),
            'Fe': (430, 438, 468, 527),
            'Tl': (535,), 'O': (686, 760),
            'He': (447, 492, 587, 667),
            'Li': (610, 670)}
print(*elements((760, 656, 430, 535, 686, 410, 468, 486)))
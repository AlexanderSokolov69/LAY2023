#!/usr/bin/env python3
# coding:utf-8
from swift import words
import random as rnd


new_words = [el.lower() for el in words]
route = {}

for el1, el2 in zip(new_words[:-2], new_words[1:]):
    if route.get(el1):
        if el2 not in route[el1]:
            route[el1] += [el2]
    else:
        route[el1] = [el2]

for i in range(20):
    sp = [rnd.choice(route["."])]
    for j in range(40):
        sp.append(rnd.choice(route[sp[-1]]))
        if sp[-1] == ".":
            break
    print(" ".join(sp).capitalize().replace(" ,", ",").
          replace(" .", ".").replace(" :", ":").replace(" ;", ";"))

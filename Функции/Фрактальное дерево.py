#!/usr/bin/env python3
# coding:utf-8
white = []
black = [white, white, white]
white.extend([black, black])

black_tree = black
print(black_tree[0])

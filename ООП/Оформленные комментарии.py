#!/usr/bin/env python3
# coding:utf-8
from sys import stdin


print(*[f'Line {row + 1}: {row_data[1:].strip()}'
        for row, row_data in enumerate(map(str.strip, stdin))
        if row_data[0] == '#'], sep='\n')

#!/usr/bin/env python3
# coding:utf-8
print(''.join([(chr(ord(s) + 32) if s < 'a' else chr(ord(s) - 32)
                ) if 'a' <= s <= 'z' or 'A' <= s <= 'Z' else s for s in input()]))

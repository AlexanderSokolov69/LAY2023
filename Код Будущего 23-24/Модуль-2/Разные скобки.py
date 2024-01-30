#!/usr/bin/env python3
# coding:utf-8
line = input()
data0 = '([{<'
data1 = ')]}>'
curr_sim = ''
stack = []
id = 0
while id < len(line):
    curr_sim = line[id]
    if curr_sim in data0:
        stack.append(curr_sim)
    else:
        if stack:
            if curr_sim == data1[data0.find(stack[-1])]:
                stack.pop()
            else:
                break
        else:
            stack.append('')
            break
    id += 1
if stack:
    print('NO')
else:
    print('YES')

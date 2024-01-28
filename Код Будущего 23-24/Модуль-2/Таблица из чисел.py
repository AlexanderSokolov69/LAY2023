#!/usr/bin/env python3
# coding:utf-8
print(*["\t".join([str(x + i * 10) for x in range(10)]) for i in range(int(input()))], sep='\n')

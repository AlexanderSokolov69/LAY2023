#!/usr/bin/env python3
# coding:utf-8
lines = [x[0] for x in sorted(
    [input().split() for _ in range(int(input()))],
    key=lambda d: ((int(d[1]) ** 2 + int(d[2]) ** 2) ** 0.5,
                   -int(d[3]),
                   int(d[1])
                   )
)]
print(*lines)

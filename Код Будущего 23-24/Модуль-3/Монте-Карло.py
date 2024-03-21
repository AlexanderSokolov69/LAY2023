from random import random

count = int(input())
in_cnt = 0
for _ in range(count):
    if (random() ** 2 + random() ** 2) ** 0.5 < 1:
        in_cnt += 1
print(4 * (in_cnt / count))

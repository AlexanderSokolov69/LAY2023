n = int(input())

numerics = [-1] + [10000] * n
for i in range(1, n + 1):
    numerics[i] = min(numerics[i], numerics[i - 1] + 1)
    if i % 2 == 0:
        numerics[i] = min(numerics[i], numerics[i // 2] + 1)
    if i % 3 == 0:
        numerics[i] = min(numerics[i], numerics[i // 3] + 1)
print(numerics)


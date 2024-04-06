with open('stone.txt', 'r') as f:
    data = [list(map(int, x.split()))
            for x in map(str.strip, f.readlines())]
col0, col1 = 0, len(data[0]) - 1
changes = []
for row, line in enumerate(data):
    if data[row][col0] >= data[row][col0 + 1]:
        data[row][col0] = data[row][col0 + 1] - 1
        changes.append((row, col0))
    if data[row][col1] >= data[row][col1 - 1]:
        data[row][col1] = data[row][col1 - 1] - 1
        changes.append((row, col1))
    print(*data[row], sep='\t')
print(*sorted(changes), sep='\n')

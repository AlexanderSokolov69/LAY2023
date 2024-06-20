s = input()
n = int(input())
for i in range(n):
    pos = 0
    while s.find('02', pos) != -1:
        pos = s.find('02', pos)
        s = s[: pos] + '22012' + s[pos + 2:]
        pos += 5
    pos = 0
    while s.find('01', pos) != -1:
        pos = s.find('01', pos)
        s = s[: pos] + '1102' + s[pos + 2:]
        pos += 4
print(len(s))


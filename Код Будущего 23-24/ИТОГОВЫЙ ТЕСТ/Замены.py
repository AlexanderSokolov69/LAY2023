# Решение 2
s = input()
n = int(input())
for i in range(n):
    pos = 0
    while s.find('011', pos) != -1:
        pos = s.find('011', pos)
        s = s[: pos] + '210220' + s[pos + 3:]
        pos += 6
    pos = 0
    while s.find('022', pos) != -1:
        pos = s.find('022', pos)
        s = s[: pos] + '201102' + s[pos + 3:]
        pos += 6
print(len(s))

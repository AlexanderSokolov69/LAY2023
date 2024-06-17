# Решение 1
def mul(ch):
    ret = 1
    for i in str(ch):
        ret *= int(i)
    return ret


print(len(
    [x for x in range(1, int(input()) + 1) if str(x)[-1] == '7' and mul(x) < 9]
))

"""
# Решение 2
s = input()
n = int(input())
for i in range(n):
    pos = 0
    while s.find('011', pos) != -1:
        pos = s.find('011', pos)
        s = s[: pos] + '210220' + s[pos + 3:]
        pos += 5
    pos = 0
    while s.find('022', pos) != -1:
        pos = s.find('022', pos)
        s = s[: pos] + '201102' + s[pos + 3:]
        pos += 6
print(len(s))
"""
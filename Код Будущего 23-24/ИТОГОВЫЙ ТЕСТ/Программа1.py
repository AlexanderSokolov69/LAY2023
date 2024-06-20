# Решение 1
def mul(ch):
    ret = 1
    for i in str(ch):
        ret *= int(i)
    return ret


print(len(
    [x for x in range(1, int(input()) + 1) if str(x)[-1] == '7' and mul(x) < 9]
))

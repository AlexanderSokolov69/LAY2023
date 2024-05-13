lb = int(input())
sp_l = [int(x) for x in input().split()]
rb = int(input())
sp_r = [int(x) for x in input().split()]
if lb > rb:
    sp_l, sp_r = sp_r.copy(), sp_l.copy()
n = 0
for el in sp_l:
    if el in sp_r:
        n += 1
        sp_r.remove(el)
print(n)

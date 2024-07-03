test = int(input())
num = 1
cnt = 0
while num < test:
    num *= 3
    cnt += 1
if num != test:
    while num > test // 2:
        cnt -= 1
        num //= 3
    while num < test:
        num *= 2
        cnt += 1
if num > test:
    cnt -= 1
    num //= 2
    while num < test:
        num += 1
        cnt += 1
print(cnt)

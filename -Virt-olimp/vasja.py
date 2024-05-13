num = int(input())
s = int(input())
start = 1
end = 3
test = 3
while end < num:
    test += end + end + 1
    if test > s:
        while test > s:
            test -= start + start + 1
            start += 2
    if test == s:
        print('YES')
        print(start)
        print(end + 1)
        break
    end += 2
else:
    print('NO')

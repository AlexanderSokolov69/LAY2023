print(len([x for x in range(1, int(input()) + 1) if x % 3 != 0 and x % 2 != sum([int(i) for i in str(x)]) % 2]))


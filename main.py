n = int(input())
c = n % 10
a = n // 100
b = n % 100 // 10

print(c, a, b)

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

if a < b:
    a, b = b, a

if (a + c) / 2 == b:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')

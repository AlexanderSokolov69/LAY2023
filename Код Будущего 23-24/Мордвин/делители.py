from sys import set_int_max_str_digits


def find_divisors(n):
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
        i += 1
    divisors_pair = [n // d for d in divisors if n // d != d]
    divisors.union(set(divisors_pair))

    return sorted(divisors)


set_int_max_str_digits(13000)
with open('2.txt') as f:
    s = f.read()
n = int(s)
#    n = int(set_int_max_str_digits(input("Введите число N: ")))
divisors = find_divisors(n)
print(f"Положительные целые делители числа {n}: {divisors}")

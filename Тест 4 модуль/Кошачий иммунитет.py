from sys import stdin


test = input()
data = map(str.strip, stdin)
print(
    *sorted(
        filter(lambda x: test.lower() in x.lower(), data),
        key=lambda x: (len(x), x),
        reverse=True
    ),
    sep='\n'
)

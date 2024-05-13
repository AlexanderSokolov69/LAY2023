from sys import stdin


print(*sorted([int(i, 3) for i in filter(
    lambda x: len(set(('3', '4', '5', '6', '7', '8', '9')) & set(x)) == 0,
    map(str.strip, stdin))
               ]
              )
      )

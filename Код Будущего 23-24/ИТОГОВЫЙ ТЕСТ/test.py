s = 'Lorem ipsum dolor sit amet'.split()
res = []

for i in range(len(s)):

   if len(s[i]) % 2 == 1:

       res.append(1)

print(sum(res))
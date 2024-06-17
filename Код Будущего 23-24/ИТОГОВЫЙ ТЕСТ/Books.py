books = {}
for _ in range(int(input())):
    book = input().split('/')
    if book[1] == 'm':
        books[book[0]] = books.get(book[0], 0) + 1
name = ''
count = 0
for b_name, cnt in books.items():
    if cnt > count:
        name = b_name
        count = cnt
print(name)

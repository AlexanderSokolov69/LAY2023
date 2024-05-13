def happy(mch, cr, data: list):
    return list(filter(lambda x: x % cr == 0 and x <= mch, data))


data = [17, 21, 80, 24, 30, 19, 10]
print(happy(30, 2, data))

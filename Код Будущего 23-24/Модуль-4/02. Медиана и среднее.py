def average(data: list[int], qual=False):  # среднее арифметическое чисел списка (без округления);
    res = sum(data) / len(data)
    if qual:
        return res
    else:
        print(res)


def median(data: list[int], qual=False):  # медиану;
    data.sort()
    length = len(data)
    sub = length // 2
    if length % 2 == 0:
        res = (data[sub] + data[sub - 1]) / 2
    else:
        res = data[sub]
    if qual:
        return res
    else:
        print(res)


def difference(data: list[int]):  # модуль разности среднего и медианы.
    res = abs(average(data, qual=True) - median(data, qual=True))
    print(res)


data = [18, 19, -6, -8, 13]
average(data)
data = [-9, 10, 17, 20, 10, 12]
median(data)
data = [6, 6, 20, 18, 5, -9, 7, 1]
difference(data)

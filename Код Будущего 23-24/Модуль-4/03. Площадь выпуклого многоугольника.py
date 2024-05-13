def polygon_square(data: list[tuple]):
    point0 = data[0]
    triangles = []
    for i in range(1, len(data) - 1):
        a = ((point0[0] - data[i][0]) ** 2 + (point0[1] - data[i][1]) ** 2) ** 0.5
        b = ((data[i][0] - data[i + 1][0]) ** 2 + (data[i][1] - data[i + 1][1]) ** 2) ** 0.5
        c = ((data[i + 1][0] - point0[0]) ** 2 + (data[i + 1][1] - point0[1]) ** 2) ** 0.5
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        triangles.append(s)
    return sum(triangles)


print(polygon_square([(12, -3), (4, -5), (-5, -4), (-6, 1), (1, 3)]))

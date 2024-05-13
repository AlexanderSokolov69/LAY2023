def point_count(p0: tuple[float, float], p1: tuple[float, float]) -> int:
    right = int(p1[0]) if int(p1[0]) < p1[0] else int(p1[0]) - 1
    left = int(p0[0]) if int(p0[0]) > p0[0] else int(p0[0]) + 1
    width = 1 + right - left
    down = int(p1[1]) if int(p1[1]) > p1[1] else int(p1[1]) + 1
    up = int(p0[1]) if int(p0[1]) < p0[1] else int(p0[1]) - 1
    height = 1 + up - down
    print(left, right, up, down)
    print(p0, p1)
    print(width, height)
    return width * height


print(point_count((2.1, 8.5), (5.6, 6.3)))
print(point_count((5, 3), (10.4, -1)))

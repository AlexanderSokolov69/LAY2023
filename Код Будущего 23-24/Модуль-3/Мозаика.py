#!/usr/bin/env python3
# coding:utf-8
from turtle import Turtle, done


def draw(bob: Turtle, name, x, y, color):
    bob.color(color)
    if name == "T":
        bob.seth(0)
        bob.goto(x - size, y)
        bob.begin_fill()
        bob.fd(size)
        bob.seth(120)
        bob.fd(size)
        bob.end_fill()
    elif name == "S":
        bob.goto(x, y)
        bob.begin_fill()
        bob.goto(x - size, y)
        bob.goto(x - size, y + size)
        bob.goto(x, y + size)
        bob.end_fill()
    elif name == "C":
        bob.goto(x - size // 2, y + size // 2)
        bob.dot(size, color)


fname = 'example.txt'  # input()
tt = Turtle()
tt.hideturtle()
tt.pu()
tt.speed(0)
with open(fname, 'r') as f:
    colors = f.readline().strip().split()
    size = int(f.readline().strip())
    figures = [list(line.strip()) for line in f.readlines()]
width = len(figures[0])
height = len(figures)
x0 = size - (width * size // 2)
y0 = height * size // 2 - size
ci = 0
clen = len(colors)
print(figures)
row = y0
for line in figures:
    col = x0
    for point in line:
        draw(tt, point, col, row, colors[ci])
        col += size
        ci = (ci + 1) % clen
    row -= size
done()

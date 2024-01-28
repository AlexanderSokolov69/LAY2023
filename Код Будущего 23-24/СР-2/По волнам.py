#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import cos, pi


def wave(tt: turtle.Turtle, angle=0):
    """ Отображение моря в текущей фазе """
    tt.pu()
    tt.clear()
    tt.goto(-350, -300)
    tt.pd()
    tt.begin_fill()
    for x in range(-349, 351):
        y = 10 * cos(0.072 * x + angle) + 15
        tt.goto(x, y)
    tt.goto(x, -300)
    tt.goto(-350, -300)
    tt.pu()
    tt.end_fill()


def boat(tt: turtle.Turtle, angle=0):
    """ Отображение лодки в текущей фазе """
    angle -= 90
    STEP = 25
    tt.reset()
    tt.ht()
    tt.clear()
    tt.color("maroon", "brown")
    tt.left(angle)
    tt.back(3 * STEP)
    tt.begin_fill()
    tt.forward(6 * STEP)
    tt.left(60)
    tt.forward(2 * STEP / cos(pi / 6))
    tt.left(120)
    tt.forward(8 * STEP)
    tt.end_fill()
    tt.pu()
    tt.back(7 * STEP)
    tt.pd()
    tt.color("gray", "lightgray")
    tt.begin_fill()
    tt.forward(4 * STEP)
    tt.right(90)
    tt.forward(8 * STEP)
    tt.end_fill()


def stopper(*pos):
    """ Завершение работы программы """
    global fstop
    fstop = False


screen = turtle.Screen()
screen.tracer(0)
more = turtle.Turtle()
more.color("blue")
more.ht()
lodka = turtle.Turtle()
fstop = True
angle = 0
boat_angle = 70
dangle = 0.1
screen.onclick(stopper)  # Ожидание клика мыши для вызова функции stopper()
while fstop:
    boat(lodka, boat_angle)
    wave(more, angle)
    angle = (angle + pi / 120) % (2 * pi)
    if boat_angle > 110:
        dangle *= -1
    if boat_angle < 70:
        dangle *= -1
    boat_angle += dangle
    screen.update()

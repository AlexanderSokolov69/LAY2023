#!/usr/bin/env python3
# coding:utf-8
import turtle
from math import sin, cos


D_SOUL = 80 * 2  # Диаметр Солнца
D_EARTH = 20 * 2  # Диаметр Земли
D_MOON = 10 * 2  # Диаметр Луны
ORB_EARTH = 270  # Орбита Земли
ORB_MOON = 60  # Орбита Луны
ANGLE_STEP_EARTH = 0.0008  # Угловая скорость Земли по орбите
ANGLE_STEP_MOON = 0.024  # Угловая скорость Луны по орбите


def create_planet(color='yellow') -> turtle.Turtle:
    """ Генератор и настройка пера рисования """
    tom = turtle.Turtle()
    tom.pu()
    tom.color(color)
    tom.ht()
    return tom


def planet_pos(angle_step, angle_current, orbit, shift_x=0, shift_y=0, angle_shift=0):
    """ Вычисление следующей позиции планеты """
    angle = (angle_current + angle_step) % 360
    x_pos = cos(angle) * orbit + shift_x
    y_pos = sin(angle) * orbit + shift_y
    return x_pos, y_pos, angle


def stopper(*pos):
    """ Завершение работы программы """
    global fstop
    fstop = False


fstop = True  # Флаг останова программы
screen = turtle.Screen()
screen.tracer(0)
screen.onclick(stopper)  # Ожидание клика мыши для вызова функции stopper()
soul = create_planet()
soul.dot(D_SOUL)
earth = create_planet(color="blue")
earth_pos = [ORB_EARTH, 0, 0]
moon = create_planet(color="burlywood")
moon_pos = [ORB_MOON + ORB_EARTH, 0, 0]
while fstop:
    earth_pos = planet_pos(ANGLE_STEP_EARTH, earth_pos[2], ORB_EARTH)
    earth.goto(earth_pos[0], earth_pos[1])
    earth.clear()
    earth.dot(D_EARTH)
    moon_pos = planet_pos(ANGLE_STEP_MOON, moon_pos[2], ORB_MOON, *earth_pos)
    moon.goto(moon_pos[0], moon_pos[1])
    moon.clear()
    moon.dot(D_MOON)
    screen.update()

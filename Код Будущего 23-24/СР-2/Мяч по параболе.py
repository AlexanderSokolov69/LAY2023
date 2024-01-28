#!/usr/bin/env python3
# coding:utf-8
import turtle


START_Y = 200
START_X = -350
D_BALL = 40
SPEED_X = 0.54
D_SPEED_Y = -0.005
BOX = [(-350, 300), (-350, -300), (350, -300), (350, 300)]
fstop = True
screen = turtle.Screen()
screen.tracer(0)
box = turtle.Turtle()
box.pu()
box.ht()
box.color("brown")
box.pensize(5)
box.goto(BOX[0])
box.pd()
for x, y in BOX:
    box.goto(x, y)
screen.update()

ball = turtle.Turtle()
ball.color("purple")
ball.pu()
ball.ht()
x = START_X + D_BALL
y = START_Y
speed_y = 0
while fstop:
    ball.clear()
    ball.goto(x, y)
    ball.dot(D_BALL)
    x += SPEED_X
    y += speed_y
    speed_y += D_SPEED_Y
    if y < BOX[1][1] + D_BALL / 2:
        speed_y *= -1
    if not (BOX[0][0] + D_BALL / 2 < x < BOX[3][0] - D_BALL / 2):
        SPEED_X *= -1
    screen.update()
turtle.done()
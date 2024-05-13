from turtle import Turtle, done, Screen


def draw(x: float, y: float):
    side = 50
    bob = Turtle()
    bob.speed(0)
    bob.ht()
    bob.pu()
    bob.goto(x - side * 0.5, y - side * 1.2)

    # bob.goto(x - side * 1.2, y - side * 0.5)
    bob.color('purple')
    bob.pd()
    bob.begin_fill()
    for i in range(8):
        bob.lt(90)
        bob.circle(-25, 180)
        bob.lt(90)
        bob.lt(360 / 8)
    bob.end_fill()
    # update()


# tracer(0)
width, height = [int(x) for x in input().split()]
sc = Screen()
sc.setup(width=width, height=height, startx=0, starty=0)
sc.onclick(draw)
sc.listen()
done()

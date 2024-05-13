from turtle import Turtle, done, numinput


SIDE = 200
colors = ['teal', 'lightseagreen', 'turquoise', 'mediumaquamarine', 'aquamarine']


def polygon(obj: Turtle, side=SIDE, n=3):
    obj.pu()
    obj.ht()
    obj.goto(-side, -side)
    obj.pd()
    obj.speed(0)
    rotate = 360 / n
    obj.begin_fill()
    for i in range(n):
        obj.fd(side)
        obj.lt(rotate)
    obj.end_fill()


n = numinput('Polygon vertices', 'Enter of number of polygon vertices',
             default=5, minval=3, maxval=12)
if not (2 < n < 13):
    n = 3
for i in range(5):
    side = SIDE - 20 * i
    bob = Turtle()
    bob.color(colors[i])
    polygon(bob, side, int(n))
done()

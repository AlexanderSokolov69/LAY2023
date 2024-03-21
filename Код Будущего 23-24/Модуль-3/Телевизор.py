from PIL import Image, ImageDraw
from turtle import Turtle, bgpic, done, tracer, update
from random import randint

w_c = int(input())
p_count = int(input())
im = Image.new('RGB', (16 * w_c, 9 * w_c), 'saddlebrown')
draw = ImageDraw.Draw(im)
draw.rectangle((w_c, w_c, 15 * w_c, 8 * w_c), 'black')
im.save('temp.png')
bgpic('temp.png')
tracer(0)
bob = Turtle()
bob.ht()
bob.pu()
bob.speed(0)
for i in range(p_count):
    bob.goto(randint(-7 * w_c, 7 * w_c),
             randint(int(-3.5 * w_c), int(3.5 * w_c)))
    bob.dot(2, 'white')
update()
done()

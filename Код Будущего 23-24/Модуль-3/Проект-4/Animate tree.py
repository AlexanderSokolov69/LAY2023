from PIL import Image
from turtle import Turtle, done, bgpic, addshape


def new_turtle(point):
    bob = Turtle()
    bob.speed(0)
    bob.ht()
    bob.pu()
    bob.goto(point[0] - 450, 450 - point[1])
    bob.shape('pic0.gif')
    bob.st()
    return bob


N_F = 7
im = Image.open('flowers.png')
w, h = im.size
w = w // N_F
for n in range(N_F):
    im_out = Image.new('RGB', (w, h))
    im_out.paste(im, (0, 0))
    im_out.save(f"pic{n}.gif", "gif")
    im = im.crop((w, 0, w * 7, h))

N_F = 5
im = Image.open('leaves.png')
w, h = im.size
w = w // N_F
for k in range(N_F):
    im_out = Image.new('RGB', (w, h))
    im_out.paste(im, (0, 0))
    im_out.save(f"pic{n + k + 1}.gif", "gif")
    im = im.crop((w, 0, w * 7, h))

pic_count = n + k + 2

bgpic('tree.png')
places = [(178, 420), (226, 202), (368,222), (538, 119), (673, 141),
          (721, 353), (635, 471), (134, 348), (289, 185), (466, 106),
          (599, 106), (734, 283), (723, 407)]

for i in range(pic_count):
    addshape(f'pic{i}.gif')
points = [[new_turtle(point), (point[0] - 450, 450 - point[1])]
          for point in places]

for n in range(pic_count - 1):
    for bob, point in points:
        bob.shape(f'pic{n + 1}.gif')

not_end = True
while not_end:
    not_end = False
    for el in range(len(points)):
        if points[el][1][1] > -400:
            not_end = True
            points[el][1] = points[el][1][0], points[el][1][1] - 20
            points[el][0].goto(*points[el][1])

done()

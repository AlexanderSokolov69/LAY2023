from PIL import Image
from turtle import Turtle, done, bgpic, setup

flower_places = [(178, 420), (226, 202), (368,222), (538, 119),
                 (673, 141), (721, 353), (635, 471)]
flover_name = 'flower'
flover_count = 7
leave_places = [(134, 348), (289, 185), (466, 106),
                (599, 106), (734, 283), (723, 407)]
leave_name = 'leave'
leave_count = 5
im = Image.open('tree.png')
size = w, h = im.size

for n in range(flover_count):
    im_out = im.copy()
    flower = Image.open(f'{flover_name}{n}.gif')
    for x, y in flower_places:
        im_out.paste(flower, (x - flower.width // 2,
                              y - flower.height // 2))
    im_out.save(f'tree{n + 1}.png')

im = Image.open('tree7.png')
leave = Image.open(f'{leave_name}{0}.gif')
for x, y in leave_places:
    im.paste(leave, (x, y - leave.height // 2))
im.save(f'tree{n + 2}.png')

im = Image.open('tree.png')
for i in range(leave_count):
    im_out = im.copy()
    leave = Image.open(f'{leave_name}{i}.gif')
    for x, y in leave_places:
        im_out.paste(leave, (x, y - leave.height // 2))
    im_out.save(f'tree{n + 3 + i}.png')

not_end = True
it = 1
while not_end:
    not_end = False
    for el in range(len(leave_places)):
        if leave_places[el][1] < h - 50:
            not_end = True
            leave_places[el] = leave_places[el][0], leave_places[el][1] + 50
            im_out = im.copy()
            for x, y in leave_places:
                im_out.paste(leave, (x, y - leave.height // 2))
            im_out.save(f'tree{n + 3 + i + it}.png')
            it += 1
pic_count = n + 3 + i + it

images = [Image.open(f'tree{i}.png') for i in range(pic_count)]
images[0].save('anim_tree.gif',
               save_all=True,  # сохранить все
               append_images=images[1:],  # добавление изображений
               optimize=True,
               duration=100,  # продолжительность анимации в мс
               loop=0)  # зацикливание

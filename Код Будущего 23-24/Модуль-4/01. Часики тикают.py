from PIL import Image


n = int(input())
im = Image.open('clock.png')
x, y = im.size
im_out = Image.new("RGB", (im.width * n, im.height), 'white')
im_new = Image.new('RGB', (x * 3, y * 3), 'white')
im_new.paste(im, (x, y))
for i in range(n):
    im = im_new.rotate(-30 * i)
    im = im.crop((x, y, 2 * x, 2 * y))
    im_out.paste(im, (i * im.width, 0))
im_out.save('ticking.png')

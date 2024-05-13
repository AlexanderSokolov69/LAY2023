from PIL import Image

im = Image.open('star.png')
width, height = im.size
n = int(input())
colors = [tuple(int(i) for i in input().split()) for _ in range(n)]
im_out = Image.new('RGB', ((n + 1) * im.width, im.height), 'white')
for i in range(n + 1):
    im_out.paste(im, (i * width + (width - im.width) // 2,
                      (height - im.height) // 2))
    if i < n:
        im = im.resize((im.width * 2 // 3, im.height * 2 // 3))
        pix = im.load()
        for x in range(im.width):
            for y in range(im.height):
                r, g, b = pix[x, y]
                if r < 255 or g < 255 or b < 255:
                    pix[x, y] = colors[i]

im_out.save('result.png')

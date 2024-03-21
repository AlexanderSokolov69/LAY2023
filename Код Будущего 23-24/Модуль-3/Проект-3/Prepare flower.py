from PIL import Image

N_F = 7
im = Image.open('flowers.png')
w, h = im.size
w = w // N_F
for n in range(N_F):
    im_out = Image.new('RGB', (w, h))
    im_out.paste(im, (0, 0))
    # im_out = im_out.convert('RGBA')
    # pix = im_out.load()
    # for x in range(w):
    #     for y in range(h):
    #         r, g, b, a = pix[x, y]
    #         if r > 250 and g > 250 and b > 250:
    #             a = 255
    #         else:
    #             a = 0
    #         pix[x, y] = r, g, b, a
    im_out.save(f"flower{n}.gif", "gif")
    im = im.crop((w, 0, w * 7, h))

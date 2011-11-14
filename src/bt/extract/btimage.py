import pygame
import bt.extract.btfile


def pal2rgb(raw_pal, pal):
    raw_rgb = bytearray(3 * len(raw_pal))
    for i, b in enumerate(raw_pal):
        raw_rgb[3 * i:3 * i + 3] = pal[b]
    return raw_rgb

def save_4bit_image(data, size, palette, dest):
    raw_pal = bytearray(2 * len(data))
    for i, b in enumerate(data):
        raw_pal[2 * i] = b >> 4
        raw_pal[2 * i + 1] = b & 0x0F
    save_8bit_image(raw_pal, size, palette, dest)


def save_8bit_image(data, size, palette, dest):
    if size == (320, 11250):
        nd = data
        for i in xrange(320):
            for j in xrange(250):
                oi = (i // 4) + (i % 4) * 80
                oi = i
                oj = (j // 4) + (j % 4) * 62
                oj = j
                nd[i + j * 320] = data[oi + oj * 320]
        data = nd

    raw_rgb = pal2rgb(data, palette)

    img = pygame.image.fromstring(str(raw_rgb), size, "RGB")
    pygame.image.save(img, dest)

def palette_grey16():
    pal = []
    for i in xrange(16):
        pal.append(bytearray([i * 16, i * 16, i * 16]))
    return pal

def palette_grey256():
    pal = []
    for i in xrange(256):
        pal.append(bytearray([i, i, i]))
    return pal

def view_size():
    return (112, 88)



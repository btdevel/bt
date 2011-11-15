import pygame
import bt.extract.btfile as btfile


def pal2rgb(raw_pal, pal):
    raw_rgb = bytearray(3 * len(raw_pal))
    for i, b in enumerate(raw_pal):
        raw_rgb[3 * i:3 * i + 3] = pal[b]
    return raw_rgb

def expand_4bit(data):
    raw = bytearray(2 * len(data))
    for i, b in enumerate(data):
        raw[2 * i] = b >> 4
        raw[2 * i + 1] = b & 0x0F
    return raw

def save_4bit_image(data, size, palette, dest):
    raw_pal = expand_4bit(data)
    save_8bit_image(raw_pal, size, palette, dest)

def print_4bit_image(data, size):
    raw_pal = expand_4bit(data)
    ind = 0
    for j in xrange(size[1]):
        for i in xrange(size[0]):
            print "%02x" % raw_pal[ind],
            ind += 1
        print

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

def save_RGB16_image(data, size, dest):
    data = expand_4bit(data)
    raw_rgb = bytearray(3 * size[0] * size[1])
    print size, len(data), len(raw_rgb)
    for i in xrange(size[0]):
        for j in xrange(size[1]):
            di = i % 2
            dj = j % 2
            order = [0, 0, 1, 1]
            order = [2, 2, 3, 3]
            order = [0, 2, 1, 3]

            linelen = 2 * size[0]
            hpos1 = order[di + 2 * dj] * (size[0] // 2)
            hpos2 = (i // 2)
            vdist = linelen * size[1] // 2
            vpos = linelen * j // 2
            hpos = hpos1 + hpos2
            b = data[vdist * 0 + hpos + vpos]
            g = data[vdist * 1 + hpos + vpos]
            r = data[vdist * 2 + hpos + vpos]
            f = data[vdist * 3 + hpos + vpos]
            def cm(c, f):
                return (c + f) * 8
            raw_rgb[(i + size[0] * j) * 3:(i + size[0] * j + 1) * 3] = [cm(r, f), cm(g, f), cm(b, f)]

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

def palette_ega16():
    ega_pal = palette_ega256()
    pal = [ega_pal[0],
           ega_pal[1],
           ega_pal[2],
           ega_pal[3],
           ega_pal[4],
           ega_pal[5],
           ega_pal[20],
           ega_pal[7],
           ega_pal[56],
           ega_pal[57],
           ega_pal[58],
           ega_pal[59],
           ega_pal[60],
           ega_pal[61],
           ega_pal[62],
           ega_pal[63],
           ]
    return pal

def palette_ega256():
    ega_pal = []
    bit = lambda b, i: (b >> i) & 1
    for i in range(64):
        b = 0x55 * (2 * bit(i, 0) + bit(i, 3))
        g = 0x55 * (2 * bit(i, 1) + bit(i, 4))
        r = 0x55 * (2 * bit(i, 2) + bit(i, 5))
        ega_pal.append(bytearray([r, g, b]))
    return ega_pal



def read_palette(name, path):
    # does not work
    data = btfile.load_file(name, path)
    pal = []
    for i in xrange(256):
        b, g, r, w = data[4 * i:4 * (i + 1)]
        r, g, b, w = data[4 * i:4 * (i + 1)]

        def cm(c, f):
#            return min(c * f, 255)
            return min((c + f) * 8, 255)
        print([cm(r, w), cm(g, w), cm(b, w)])
        pal.append(bytearray([cm(r, w), cm(g, w), cm(b, w)]))
    return pal



def view_size():
    return (112, 88)



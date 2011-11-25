import pygame
import bt.extract.btfile as btfile


def show(im):
    pygame.init()
    pygame.display.init()
    pygame.font.init()

    pygame.display.set_mode(im.get_size())
    s = pygame.display.get_surface()
    s.blit(im, (0, 0))
    pygame.display.flip()
    stop = False
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                stop = True
            elif event.type == pygame.QUIT:
                stop = True
    pygame.display.quit()

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

def expand_2bit(data):
    raw = bytearray(4 * len(data))
    for i, b in enumerate(data):
        raw[4 * i + 0] = (b >> 6) & 0x03
        raw[4 * i + 1] = (b >> 4) & 0x03
        raw[4 * i + 2] = (b >> 2) & 0x03
        raw[4 * i + 3] = (b >> 0) & 0x03
    return raw

def save_4bit_image(data, size, palette, dest=None):
    raw_pal = expand_4bit(data)
    return save_8bit_image(raw_pal, size, palette, dest)

def print_4bit_image(data, size):
    raw_pal = expand_4bit(data)
    ind = 0
    for j in xrange(size[1]):
        for i in xrange(size[0]):
            print "%02x" % raw_pal[ind],
            ind += 1
        print

def double_scale(data, size, n):
    w, h = size[0], size[1]
    buffer = bytearray(4 * w * h)
    for i in xrange(h):
        for j in xrange(w):
            src = (i * w + j) * n
            dst = (4 * i * w + 2 * j) * n
            buffer[dst:dst + 2 * n] = data[src:src + n] * 2
            dst = ((4 * i + 2) * w + 2 * j) * n
            buffer[dst:dst + 2 * n] = data[src:src + n] * 2
    return buffer, (2 * w, 2 * h)


def save_8bit_image(data, size, palette, dest=None):
    data = data[:size[0] * size[1]] # make optional
    data, size = double_scale(data, size, 1)
    raw_rgb = pal2rgb(data, palette)
    img = pygame.image.fromstring(str(raw_rgb), size, "RGB")

    if dest:
        pygame.image.save(img, dest)
    return img

def save_4bit_separated_image(data, size, dest=None):
    raw = bytearray(size[0] * size[1])
    bit = lambda b, i: (b >> i) & 1
    vdist = size[1] * (size[0] // 8)
    for i in xrange(size[0]):
        for j in xrange(size[1]):
            ind = (i // 8) + j * (size[0] // 8)
            nb = 7 - i % 8
            b0 = bit(data[ind + 0 * vdist], nb)
            b1 = bit(data[ind + 1 * vdist], nb)
            b2 = bit(data[ind + 2 * vdist], nb)
            b3 = bit(data[ind + 3 * vdist], nb)
            raw[i + j * size[0]] = (b3 << 3) + (b2 << 2) + (b1 << 1) + (b0 << 0)
    return save_8bit_image(raw, (size[0], size[1]), palette_cga16(), dest)

def save_4bit_partitioned_image(data, parts, pal, namepattern):
    for part in range(len(parts)):
        s = 0
        for i in range(part):
            s += (parts[i][0] * parts[i][1])
        w = parts[part][0]
        h = parts[part][1]
        if part == len(parts) - 1:
            rem = len(data) - s // 2 - (w * h) // 2
            if rem != 0:
                print "Remaning bytes:", rem
        subdata = data[s // 2:(s + w * h) // 2]
        save_4bit_image(subdata, (w, h), pal, namepattern % part)

def save_2bit_interlaced_image(data, size, palette, dest=None):
    raw_pal = expand_2bit(data)
    w, h = size[0], size[1]
    buffer = bytearray(w * h)
    d = len(raw_pal) // 2
    for i in xrange(h):
        start = (i % 2) * d + (i // 2) * w
        buffer[i * w:i * w + w] = raw_pal[start:start + w]
    return save_8bit_image(buffer, size, palette, dest)

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

def palette_cga8(palnum, high):
    pal16 = palette_cga16()

    if (palnum, high) == (0, False):
        ind = [0, 2, 4, 6]
    elif (palnum, high) == (0, True):
        ind = [0, 10, 12, 14]
    elif (palnum, high) == (1, False):
        ind = [0, 3, 5, 7]
    elif (palnum, high) == (1, True):
        ind = [0, 11, 13, 15]
    else:
        # use 1, False as default (should give a warning)
        ind = [0, 3, 5, 7]
    return [pal16[j] for j in ind]


def palette_cga16():
    ega_pal = palette_ega64()
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

def palette_ega64():
    ega_pal = []
    bit = lambda b, i: (b >> i) & 1
    for i in range(64):
        b = 0x55 * (2 * bit(i, 0) + bit(i, 3))
        g = 0x55 * (2 * bit(i, 1) + bit(i, 4))
        r = 0x55 * (2 * bit(i, 2) + bit(i, 5))
        ega_pal.append(bytearray([r, g, b]))
    return ega_pal


def view_size():
    return (112, 88)



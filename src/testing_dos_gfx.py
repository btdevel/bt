import os

import bt.extract.btfile as btfile
import bt.extract.btimage as btimage

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")


# levels
if False:
    btfile.show_indexed_file_info("levs", msdos_bt1_path)
    data = btfile.load_indexed_file("levs", msdos_bt1_path)

# images
pal16 = btimage.palette_cga16()
pal16g = btimage.palette_grey16()
pal64 = btimage.palette_ega64()
pal256 = btimage.palette_grey256()
vsize = btimage.view_size()



save_8bit_image = btimage.save_8bit_image
def expand_2bit(data):
    raw = bytearray(4 * len(data))
    for i, b in enumerate(data):
        raw[4 * i + 0] = (b >> 6) & 0x03
        raw[4 * i + 1] = (b >> 4) & 0x03
        raw[4 * i + 2] = (b >> 2) & 0x03
        raw[4 * i + 3] = (b >> 0) & 0x03
    return raw

def save_2bit_image(data, size, palette, dest=None):
    raw_pal = expand_2bit(data)
    return save_8bit_image(raw_pal, size, palette, dest)

def save_2bit_separated_image(data, size, dest=None):
    raw = bytearray(size[0] * size[1])
    bit = lambda b, i: (b >> i) & 1
    vdist = size[1] * (size[0] // 8)+30
    vdist=len(data)//2
    for i in xrange(size[0]):
        for j in xrange(size[1]):
            ind = (i // 8) + j * (size[0] // 8)
            nb = 7 - i % 8
            b0 = 1*bit(data[ind + 0 * vdist], nb)
            b1 = 1*bit(data[ind + 1 * vdist], nb)
            raw[i + j * size[0]] = (b1 << 1) + (b0 << 0)
    return save_8bit_image(raw, (size[0], size[1]), btimage.palette_cga8(1, False), dest)


if True:
    infilename = "b0.huf"
    outfilename = "b0.png"
    btfile.show_compressed_file_info(infilename, msdos_bt1_path)
    data = btfile.load_compressed_file(infilename, msdos_bt1_path)
    im = btimage.save_4bit_image(data, vsize, pal16, outfilename)
    import PIL
    from PIL import Image
    import pygame
    pim = Image.fromstring("RGB", im.get_size(), pygame.image.tostring(im, "RGB"))
    sz=im.get_size()
    sz = (2*sz[0], 2*sz[1])
    #pim = pim.resize(sz, Image.NEAREST)
    pim = pim.resize(sz, Image.BICUBIC)
    ll = (10, 10)
    ul = (10, 100)
    lr = (100, 10)
    ur = (100, 100)

    ll = (sz[0], sz[1])
    ul = (sz[0], 0)
    lr = (0-100, sz[1]+100)
    ur = (0, -100)
    (x0, y0, x1, y1, x2, y2, y3, y3) = ul + ll + lr + ur
    pim = pim.transform(sz,Image.QUAD,(x0, y0, x1, y1, x2, y2, y3, y3))

    pim.show()
    print im



if False:
    # does not work
    btfile.show_compressed_file_info("rgb_tit", msdos_bt1_path)
    data = btfile.load_compressed_file("rgb_tit", msdos_bt1_path)

    save_2bit_separated_image(data, (640, 100), "rgb_tit.png")
    #btimage.save_separated_image(data, (64, 64), "rgb_tit2.png")
    rgbdata = data

if False:
    # does not work
    #btfile.show_indexed_file_info("bigpic", msdos_bt1_path)
    #data = btfile.load_indexed_file("bigpic", msdos_bt1_path)
    data0 = btfile.load_indexed_file("bigpic", msdos_bt1_path, index=3)

    print
    for i, c  in enumerate(list(data0)):
        if i % 16 == 0: print
        print hex(c),
        #if i > 256: break
    print
    #btimage.save_4bit_image(data, (w, h), pal16, "bigpic0-foo.png")
    # btimage.save_8bit_image(data, (w, h), pal64, "bigpic0-foo.png")


if False:
    # works

    # house fronts "b?.huf"
    for i in xrange(4):
        infilename = "b%d.huf" % i
        outfilename = "b%d.png" % i
        btfile.show_compressed_file_info(infilename, msdos_bt1_path)
        data = btfile.load_compressed_file(infilename, msdos_bt1_path)
        btimage.save_4bit_image(data, vsize, pal16, outfilename)

    # game screen "bardscr", title screen "bardtit"
    for basename in ["bardscr", "bardtit"]:
        btfile.show_compressed_file_info(basename, msdos_bt1_path)
        data = btfile.load_compressed_file(basename, msdos_bt1_path)
        btimage.save_4bit_separated_image(data, (320, 200), basename + ".png")

    # dungeon wall tiles "dpics?"
    parts = [(56, 88), (192, 86), (120, 54), (80, 33), (48, 17),
             (16, 40), # unclear (portals?)
             (32, 88), (48, 85), (32, 52), (16, 31), (16, 15),
             (48, 32), (40, 18),
             (80, 8) # unclear (far away wall? where used?)
             ]

    for i in xrange(3):
        basename = "dpics%d" % i
        btfile.show_compressed_file_info(basename, msdos_bt1_path)
        data0 = btfile.load_compressed_file(basename, msdos_bt1_path)
        btimage.save_4bit_partitioned_image(data0, parts, pal16, basename + "-%02d.png")


# 47 image of inside adv guild
# images from city in bigpics (houses except front, inside house)
# dungeons are in dpics0, dpics1, dpics2

print "Done"

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
pal16 = btimage.palette_ega16()
pal16g = btimage.palette_grey16()
pal64 = btimage.palette_ega64()
pal256 = btimage.palette_grey256()
vsize = btimage.view_size()

if False:
    # works
    for i in xrange(0, 4):
        infilename = "b%d.huf" % i
        outfilename = "b%d.png" % i
        btfile.show_compressed_file_info(infilename, msdos_bt1_path)
        data = btfile.load_compressed_file(infilename, msdos_bt1_path)
        btimage.save_4bit_image(data, vsize, pal16, outfilename)

if False:
    # works
    btfile.show_compressed_file_info("bardscr", msdos_bt1_path)
    data = btfile.load_compressed_file("bardscr", msdos_bt1_path)
    btimage.save_separated_image(data, (320, 200), "bardscr.png")

    btfile.show_compressed_file_info("bardtit", msdos_bt1_path)
    data = btfile.load_compressed_file("bardtit", msdos_bt1_path)
    btimage.save_separated_image(data, (320, 200), "bardtit.png")

if False:
    # does not work
    btfile.show_compressed_file_info("rgb_tit", msdos_bt1_path)
    data = btfile.load_compressed_file("rgb_tit", msdos_bt1_path)
    btimage.save_4bit_image(data, (256, 128), pal16, "rgb_tit.png")
    btimage.save_separated_image(data, (64, 64), "rgb_tit2.png")
    rgbdata = data

if True:
    # does not work
    #btfile.show_indexed_file_info("bigpic", msdos_bt1_path)
    #data = btfile.load_indexed_file("bigpic", msdos_bt1_path)
    data0 = btfile.load_indexed_file("bigpic", msdos_bt1_path, index=3)

    for i, c  in enumerate(list(data0)):
        if i % 16 == 0: print
        print hex(c),
        if i > 256: break

    data = []
    mult = 1
    for c in data0:
        if c >= 0x80:
            mult = c - 0x80
        else:
            data = data + [c, ] * mult
            mult = 1
    print
    print len(data)
    w = 112
    h = 544
    data = data[:w * h // 2]

    btimage.save_4bit_image(data, (w, h), pal16, "bigpic0-foo.png")
    # btimage.save_8bit_image(data, (w, h), pal64, "bigpic0-foo.png")


if True:
    # works
    parts = [(56, 88), (192, 86), (120, 54), (80, 33), (48, 17),
             (16, 40), # unclear
             (32, 88), (48, 85), (32, 52), (16, 31), (16, 15),
             (48, 32), (40, 18),
             (80, 8) # unclear
             ]

    btfile.show_compressed_file_info("dpics0", msdos_bt1_path)
    data0 = btfile.load_compressed_file("dpics0", msdos_bt1_path)
    btimage.save_4bit_partitioned_image(data0, parts, pal16, "dpics0-%02d.png")

    btfile.show_compressed_file_info("dpics1", msdos_bt1_path)
    data1 = btfile.load_compressed_file("dpics1", msdos_bt1_path)
    btimage.save_4bit_partitioned_image(data1, parts, pal16, "dpics0-%02d.png")

    btfile.show_compressed_file_info("dpics2", msdos_bt1_path)
    data2 = btfile.load_compressed_file("dpics2", msdos_bt1_path)
    btimage.save_4bit_partitioned_image(data2, parts, pal16, "dpics0-%02d.png")

# 47 image of inside adv guild
# images from city in bigpics (houses except front, inside house)
# dungeons are in dpics0, dpics1, dpics2

print "Done"

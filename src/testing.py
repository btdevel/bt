import os

import bt.extract.btfile as btfile
import bt.extract.btimage as btimage

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")


# levels
btfile.show_indexed_file_info("levs", msdos_bt1_path)
data = btfile.load_indexed_file("levs", msdos_bt1_path)


# images

pal = btimage.palette_ega16()
pal256 = btimage.palette_ega256()
vsize = btimage.view_size()

for i in xrange(0, 4):
    infilename = "b%d.huf" % i
    outfilename = "b%d.png" % i
    btfile.show_compressed_file_info(infilename, msdos_bt1_path)
    data = btfile.load_compressed_file(infilename, msdos_bt1_path)
    btimage.save_4bit_image(data, vsize, pal, outfilename)

if True:
    btfile.show_compressed_file_info("bardscr", msdos_bt1_path)
    data = btfile.load_compressed_file("bardscr", msdos_bt1_path)
    btimage.save_RGB16_image(data, (160, 100), "bardscr.png")

    btfile.show_compressed_file_info("bardtit", msdos_bt1_path)
    data = btfile.load_compressed_file("bardtit", msdos_bt1_path)
    btimage.save_RGB16_image(data, (160, 100), "bardtit.png")

if False:
    btfile.show_compressed_file_info("rgb_tit", msdos_bt1_path)
    data = btfile.load_compressed_file("rgb_tit", msdos_bt1_path)
    btimage.save_4bit_image(data, (256, 128), pal, "rgb_tit.png")
    rgbdata = data
if False:
    btfile.show_indexed_file_info("bigpic", msdos_bt1_path)
    data = btfile.load_indexed_file("bigpic", msdos_bt1_path)
    btimage.save_4bit_image(data[0], (4 * 29, 79), pal, "bigpic0.png")


if False:
    btfile.show_compressed_file_info("dpics0", msdos_bt1_path)
    data0 = btfile.load_compressed_file("dpics0", msdos_bt1_path)
    btfile.show_compressed_file_info("dpics1", msdos_bt1_path)
    data1 = btfile.load_compressed_file("dpics1", msdos_bt1_path)
    btfile.show_compressed_file_info("dpics2", msdos_bt1_path)
    data2 = btfile.load_compressed_file("dpics2", msdos_bt1_path)


    btimage.save_4bit_image(data0, (72 * 2, 307), pal, "dpics0.png")
    btimage.save_4bit_image(data1, (72 * 2, 307), pal, "dpics1.png")
    btimage.save_4bit_image(data2, (72 * 2, 307), pal, "dpics2.png")


    foo = []
    for i in xrange(48):
        foo += data0[i::48]
    foo = data0[13:] + data0[:13]
    btimage.save_8bit_image(data0, (72, 307), pal256, "dpics0b.png")
    btimage.save_8bit_image(foo, (72, 307), pal256, "dpics0c.png")


    #screen = btfile.rle_decode(data2)
    #xxx = bytearray(sum(screen, []))
    #btimage.save_4bit_image(xxx, (128 * 2, 160), pal, "dpics2.png")


# 47 image of inside adv guild
# images from city in bigpics (houses except front, inside house)
# dungeons are in dpics0, dpics1, dpics2

print "Done"

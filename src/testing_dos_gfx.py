import os

import bt.extract.btfile as btfile
import bt.extract.btimage as btimage

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")


# images
pal16 = btimage.palette_cga16()
pal16g = btimage.palette_grey16()
pal64 = btimage.palette_ega64()
pal256 = btimage.palette_grey256()
vsize = btimage.view_size()


if True:
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


if True:
    # works
    show = lambda im: btimage.show(im)

    # house fronts "b?.huf"
    for i in xrange(4):
        infilename = "b%d.huf" % i
        outfilename = "b%d.png" % i
        btfile.show_compressed_file_info(infilename, msdos_bt1_path)
        data = btfile.load_compressed_file(infilename, msdos_bt1_path)
        im = btimage.save_4bit_image(data, vsize, pal16, outfilename)
        show(im)

    # game screen "bardscr", title screen "bardtit"
    for basename in ["bardscr", "bardtit"]:
        btfile.show_compressed_file_info(basename, msdos_bt1_path)
        data = btfile.load_compressed_file(basename, msdos_bt1_path)
        im = btimage.save_4bit_separated_image(data, (320, 200), basename + ".png")
        show(im)

    # game screen "cga_scr", title screen "rgb_tit"
    for basename in [ "cga_scr", "rgb_tit"]:
        btfile.show_compressed_file_info(basename, msdos_bt1_path)
        data = btfile.load_compressed_file(basename, msdos_bt1_path)
        im = btimage.save_2bit_interlaced_image(data, (320, 200), btimage.palette_cga8(1, True), basename + ".png")
        show(im)


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

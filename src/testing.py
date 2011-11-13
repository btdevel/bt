import os

import bt.extract.btfile as btfile

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")
amiga_bt1_path = os.path.join(res_path, "amiga", "bt1", "bards_data")

btfile.show_indexed_file_info("levs", msdos_bt1_path)
btfile.show_indexed_file_info("levs", amiga_bt1_path)

btfile.show_compressed_file_info("b0.huf", msdos_bt1_path)

data = btfile.load_compressed_file("b0.huf", msdos_bt1_path)
print data[:10]
print len(data)

import pygame
raw_pal = bytearray(2 * len(data))
for i, b in enumerate(data):
    raw_pal[2 * i] = b >> 4
    raw_pal[2 * i + 1] = b & 0x0F

pal = []
for i in xrange(16):
    pal.append(bytearray([i * 16, i * 16, i * 16]))


raw_rgb = bytearray(3 * len(raw_pal))
for i, b in enumerate(raw_pal):
    raw_rgb[3 * i:3 * i + 3] = pal[b]

img = pygame.image.fromstring(str(raw_rgb), (112, 88), "RGB")
pygame.image.save(img, "foo.png")



import os

import bt.extract.btfile as btfile
import bt.extract.btimage as btimage

res_path = os.path.join("..", "res")
amiga_bt1_path = os.path.join(res_path, "amiga", "bt1", "bards_data")


# levels
#btfile.show_indexed_file_info("levs", amiga_bt1_path)
data = btfile.load_indexed_file("levs", amiga_bt1_path)

if True:
    btfile.show_compressed_file_info("bard_screen", amiga_bt1_path)
    data = btfile.load_compressed_file("bard_screen", amiga_bt1_path)
    #btimage.save_4bit_image(data, (320, 250), pal, "bard_screen.png")

if True:
    btfile.show_compressed_file_info("icon0", amiga_bt1_path)
    btfile.show_compressed_file_info("icon1", amiga_bt1_path)
    btfile.show_compressed_file_info("icon2", amiga_bt1_path)
    data = btfile.load_compressed_file("icon0", amiga_bt1_path)
    data = btfile.load_compressed_file("icon2", amiga_bt1_path)

if False:
    btfile.show_indexed_file_info("pics", amiga_bt1_path)
    data = btfile.load_indexed_file("pics", amiga_bt1_path)

btfile.show_compressed_file_info("big_city", amiga_bt1_path)
data = btfile.load_compressed_file("big_city", amiga_bt1_path)
btfile.show_compressed_file_info("big_dung", amiga_bt1_path)

btfile.show_compressed_file_info("CITY/bi1", amiga_bt1_path)
data1 = btfile.load_compressed_file("CITY/bi1", amiga_bt1_path)
btfile.show_compressed_file_info("CITY/bi2", amiga_bt1_path)
data2 = btfile.load_compressed_file("CITY/bi2", amiga_bt1_path)
btfile.show_compressed_file_info("CITY/BI3", amiga_bt1_path)
data3 = btfile.load_compressed_file("CITY/BI3", amiga_bt1_path)

# 

print "Done"

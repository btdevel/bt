import os

import bt.extract.btfile as btfile
import bt.extract.btimage as btimage

res_path = os.path.join("..", "res")
amiga_bt1_path = os.path.join(res_path, "amiga", "bt1", "bards_data")


# levels
#btfile.show_indexed_file_info("levs", amiga_bt1_path)
data = btfile.load_indexed_file("levs", amiga_bt1_path)


btfile.show_compressed_file_info("CITY/bi1", amiga_bt1_path)
data1 = btfile.load_compressed_file("CITY/bi1", amiga_bt1_path)
btfile.show_compressed_file_info("CITY/bi2", amiga_bt1_path)
data2 = btfile.load_compressed_file("CITY/bi2", amiga_bt1_path)
btfile.show_compressed_file_info("CITY/BI3", amiga_bt1_path)
data3 = btfile.load_compressed_file("CITY/BI3", amiga_bt1_path)

# 

print "Done"

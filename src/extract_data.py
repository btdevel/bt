"""
Extract data from binary memdump file (MEMDUMP.BIN) of running BARD.EXE
and write into python files. 
"""

import bt.extract.bt1.data as bt1data

bt1data.load_item_data("../content/msdos/Bard1")


"""
Extract data from binary memdump file (MEMDUMP.BIN) of running BARD.EXE
and write into python files. 

@author: ezander
"""

import bt.extract.item_data as item_data

item_data.load_item_data("../content/msdos/Bard1")


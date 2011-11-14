from bt.extract.btfile import load_compressed_file, load_indexed_file

def read_level(level, path):
    "Read a BT1 level (0=Wine Cellar,4=Catacombs1,7=Castle1,10=Kylearan,11=Mangar1,15=Mangar5) from disk and decode it."
    return load_indexed_file('levs', path, level)

def read_city_path(path):
    "Read BT1 city path file and decode it."
    return load_compressed_file('city.pat', path)

def read_city_name(path):
    "Read BT1 city path file and decode it."
    return load_compressed_file('city.nam', path)


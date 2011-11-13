def read_level(level):
    "Read a BT1 level (0=Wine Cellar,4=Catacombs1,7=Castle1,10=Kylearan,11=Mangar1,15=Mangar5) from disk and decode it."
    inp = load_file("levs")
    offset = read_long(inp, level * 4)
    return decode_from_offset(inp, offset)

def read_city_path():
    "Read BT1 city path file and decode it."
    inp = load_file("city.pat")
    return decode_from_offset(inp, offset=0)

def read_city_name():
    "Read BT1 city path file and decode it."
    inp = load_file("city.nam")
    return decode_from_offset(inp, offset=0)


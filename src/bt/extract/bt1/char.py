import struct

import bt.extract.btfile as btfile
import bt.char as btchar

fields_msdos = [("name", ">14s  2x"),
                ("char_party", "B"),
                ("status", "B"),
                ("race", "xB"),
                ("char_class", "xB"),
                ("curr_str", "xB"),
                ("curr_int", "xB"),
                ("curr_dex", "xB"),
                ("curr_con", "xB"),
                ("curr_lck", "xB"),
                ("max_str", "xB"),
                ("max_int", "xB"),
                ("max_dex", "xB"),
                ("max_con", "xB"),
                ("max_lck", "xB3x"),
                ("max_hp", "H"),
                ("curr_hp", "H"),
                ("max_sp", "H"),
                ("curr_sp", "H"),
                ("equipment", "16s"),
                ("experience", "L"),
                ("gold", "L"),
                ("level", "H"),
                ("con_level", "3xB"),
                ("mag_level", "B"),
                ("sor_level", "B"),
                ("wiz_level", "B7x"),
                ("num_songs", "B15x")
                ]


def fill_fields_from_buffer(char, fields, buffer):
    offset = 0
    buffer = bytes(buffer)
    for field in fields:
        attr_name, fmt = field
        value = struct.unpack_from(fmt, buffer, offset)
        char.__setattr__(attr_name, value[0])
        offset += struct.calcsize(fmt)

def load_msdos_character(id, path):
    if isinstance(id, str):
        raise Exception("Not yet implemented")

    char = btchar.Character(id)
    ba = btfile.load_file(str(id) + ".TPW", path)

    fill_fields_from_buffer(char, fields_msdos, ba)
    return char

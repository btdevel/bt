import glob
import struct

import bt.extract.btfile as btfile
import bt.char as btchar

base_fields  = [("name", ">14s  2x"),
                ("char_party", "B")]

char_fields  = [("name", ">14s  2x"),
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

party_fields = [("name", ">14s  2x"),
                ("char_party", "B"),
                ("name1", ">14s  2x"),
                ("name2", ">14s  2x"),
                ("name3", ">14s  2x"),
                ("name4", ">14s  2x"),
                ("name5", ">14s  2x"),
                ("name6", ">14s  2x")]


def fill_fields_from_buffer(char, fields, buffer):
    offset = 0
    buffer = bytes(buffer)
    for field in fields:
        attr_name, fmt = field
        value = struct.unpack_from(fmt, buffer, offset)[0]
        if isinstance(value, str):
            value=value.split("\0")[0]
        char.__setattr__(attr_name, value)
        offset += struct.calcsize(fmt)

def load_character(filename):
    info = load_base_info(filename)
    if info.is_party:
        return load_party(filename)

    ba = btfile.load_file(filename)
    char = btchar.Character()
    fill_fields_from_buffer(char, char_fields, ba)
    return char

def load_character_by_name(btpath, name):
    char_list = get_char_list(btpath)
    for char in char_list:
        if char.name==name:
            return load_character(char.filename)
    return None

def load_party(filename):
    ba = btfile.load_file(filename)
    party = btchar.Party()
    fill_fields_from_buffer(party, party_fields, ba)
    return party

def load_base_info(filename):
    ba = btfile.load_file(filename)
    char = btchar.Character(id)
    fill_fields_from_buffer(char, base_fields, ba)
    char_info = btchar.CharPartyBase(char.char_party == 2)
    char_info.name = char.name
    char_info.filename = filename
    return char_info

def get_char_list(btpath):
    files = glob.glob(btpath + "/*.TPW")
    filelist = []
    for filename in files:
        char = load_base_info(filename)
        filelist.append(char)

    return filelist

#In config: char_loader = bt.extract.bt1.char_msdos.Loader
class Loader(object):
    def __init__(self, char_path):
        self.char_path = char_path
        
    def char_list(self):
        return get_char_list(self.char_path)

    def load_char(self, filename):
        return load_character(filename)

    def load_char_by_name(self, name):
        return load_character_by_name(self.char_path, name)

    def save_char(self):
        raise NotImplemented

    def __str__(self):
        return "MSDOS loader for BT1 (path='%s')" % self.char_path


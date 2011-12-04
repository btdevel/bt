import bt.extract.btfile as btfile
import bt.extract.btdata as btdata
import bt.char as btchar

msdos_executable = "bard.exe"
memdump = "MEMDUMP.BIN"

def load_strings_by_identifier(bt_path, identifier, num):
    ba = btfile.load_file_cached(msdos_executable, bt_path)
    return btdata.get_string_data(ba, identifier, num)


def load_street_names(bt_path):
    streets = load_strings_by_identifier(bt_path, 'Alley\x00Rakhir', 20)
    streets += [None, ] * (0x100 - len(streets))
    streets[0xFF] = "Grand Plaz"
    return streets

def load_statue_names(bt_path):
    return load_strings_by_identifier(bt_path, 'the statue of', 5)

def load_monster_names(bt_path):
    return load_strings_by_identifier(bt_path, 'Kobold^^s^', 127)

def load_item_names(bt_path):
    return load_strings_by_identifier(bt_path, 'Torch\x00Lamp', 127)

def load_itemtype_names(bt_path):
    return load_strings_by_identifier(bt_path, 'Item\x00Weapon', 11)

def load_class_names(bt_path):
    return load_strings_by_identifier(bt_path, 'Warrior\x00Paladin', 10)

def load_classes(bt_path):
    names = load_class_names(bt_path)
    for id, name in enumerate(names):
        btchar.CharacterClass(id, name)

def load_race_names(bt_path):
    return load_strings_by_identifier(bt_path, 'Human\x00Elf', 7)

def load_races(bt_path):
    names = load_race_names(bt_path)
    for id, name in enumerate(names):
        btchar.CharacterRace(id, name)

def load_item_data(bt_path):
    ba = btfile.load_file_cached(memdump, bt_path)
    num = 128

    start = ba.find('\x00\xFF\xFF\x8E\x9E') + num
    def get_values(start_ind):
        return ba[start_ind + 1:start_ind + num]

    effects = get_values(start)
    print list(effects)

    equip = get_values(start-num)
    print list(equip)

    special = get_values(start-2*num)
    print list(special)

    acbonus = get_values(start-3*num)
    print list(acbonus)

    basdam = get_values(start-4*num)
    print list(basdam)


    names = load_item_names(bt_path)

    assert names[0] == "Torch"
    assert names[-1] == "Spectre Snare"

    class Item(object):
        def __init__(self, name, effects, equip, special, ac, bonus,):
            pass



    types = load_itemtype_names(bt_path)
    items = []
    for i in xrange(0*num - 1):
        type = special[i] & 0x0F
        spec_attack = (special[i] & 0xF0) >> 4
        effect = effects[i]
        num_dice = (basdam[i] & 0x0F) + 1
        dice_sides = [4, 6, 8, 12, 16][(basdam[i] & 0xF0) >> 4]
        print "(%02x) %s: %s, dam=%dd%d " % (i, names[i], types[type], num_dice, dice_sides)







import os

def load_string_data(ba, ident, num):
    data = [None] * num
    start = ba.find(ident)
    for i in xrange(num):
        end = ba.find('\x00', start)
        data[i] = str(ba[start:end])
        start = end + 1
    return data

def load_streets(bt_dir):
    filename = os.path.join(bt_dir, "bard.exe")
    f = open(filename, "rb")
    ba = bytearray(f.read())

    streets = load_string_data(ba, 'Alley\x00Rakhir', 20)
    return streets


def load_item_data(bt_dir):
    filename = os.path.join(bt_dir, "bard.exe")
    f = open(filename, "rb")
    ba = bytearray(f.read())
    num = 128

    start = ba.find('\x00\xFF\xFF\x8E\x9E') + num
    effects = ba[start + 1:start + num]
    start = start - 128
    equip = ba[start + 1:start + num]
    start = start - 128
    special = ba[start + 1:start + num]
    start = start - 128
    acbonus = ba[start + 1:start + num]
    start = start - 128
    basdam = ba[start + 1:start + num]

    names = load_string_data(ba, 'Torch\x00Lamp', 127)
    types = load_string_data(ba, 'Item\x00Weapon', 11)

    classes = load_string_data(ba, 'Warrior\x00Paladin', 10)
    races = load_string_data(ba, 'Human\x00Elf', 7)
    monsters = load_string_data(ba, 'Kobold^^s^', 127)
    states = load_string_data(ba, 'DEAD\x00STON', 7)
    streets = load_string_data(ba, 'Alley\x00Rakhir', 20)
    statues = load_string_data(ba, 'the statue of', 5)
    daytimes = load_string_data(ba, 'the statue of', 5)


    print classes
    print races
    print monsters
    print states
    print streets + ["Grand Plaz", ]
    print statues
    return

    assert names[0] == "Torch"
    assert names[-1] == "Spectre Snare"

    class Item(object):
        def __init__(self, name, effects, equip, special, ac, bonus,):
            pass

    items = []
    for i in xrange(num - 1):
        type = special[i] & 0x0F
        spec_attack = (special[i] & 0xF0) >> 4
        effect = effects[i]
        num_dice = (basdam[i] & 0x0F) + 1
        dice_sides = [4, 6, 8, 12, 16][(basdam[i] & 0xF0) >> 4]
        print "(%02x) %s: %s, dam=%dd%d " % (i, names[i], types[type], num_dice, dice_sides)


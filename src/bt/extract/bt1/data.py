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
    effects = ba[start + 1:start + num]
    start = start - 128
    equip = ba[start + 1:start + num]
    start = start - 128
    special = ba[start + 1:start + num]
    start = start - 128
    acbonus = ba[start + 1:start + num]
    start = start - 128
    basdam = ba[start + 1:start + num]

    names = load_item_names(bt_path)

    assert names[0] == "Torch"
    assert names[-1] == "Spectre Snare"

    class Item(object):
        def __init__(self, name, effects, equip, special, ac, bonus,):
            pass

    types = load_itemtype_names(bt_path)
    items = []
    for i in xrange(num - 1):
        type = special[i] & 0x0F
        spec_attack = (special[i] & 0xF0) >> 4
        effect = effects[i]
        num_dice = (basdam[i] & 0x0F) + 1
        dice_sides = [4, 6, 8, 12, 16][(basdam[i] & 0xF0) >> 4]
        print "(%02x) %s: %s, dam=%dd%d " % (i, names[i], types[type], num_dice, dice_sides)






# 00h=Human
# 01h=Elf
# 02h=Dwarf
# 03h=Hobbit
# 04h=Half-Elf
# 05h=Half-orc
# 06h=Gnome
# 00h=Warrior
# 01h=Paladin
# 02h=Rogue
# 03h=Bard
# 04h=Hunter
# 05h=Monk
# 06h=Conjurer
# 07h=Magician
# 08h=Sorceror
# 09h=Wizard



# Item     Code #
# (none)     0x00
# Torch     0x01
# Lamp     0x02
# Broadsword     0x03
# Short Sword     0x04
# Dagger     0x05
# War Axe     0x06
# Halbard     0x07
# Mace     0x08
# Staff     0x09
# Buckler     0x0A
# Tower Shield     0x0B
# Leather Armor     0x0C
# Chain Mail     0x0D
# Scale Armor     0x0E
# Plate Armor     0x0F
# Robes     0x10
# Helm     0x11
# Leather Glvs     0x12
# Gauntlets     0x13
# Mandolin     0x14
# Harp     0x15
# Flute     0x16
# Mthr Sword     0x17
# Mthr Shield     0x18
# Mthr Chain     0x19
# Mthr Scale     0x1A
# Samurai Fgn     0x1B
# Bracers [6]     0x1C
# Bardsword     0x1D
# Fire Horn     0x1E
# Lightwand     0x1F
# Mthr Dagger     0x20
# Mthr Helm     0x21
# Mthr Gloves     0x22
# Mthr Axe     0x23
# Mthr Mace     0x24
# Mthr Plate     0x25
# Ogre Fgn     0x26
# Lak's Lyre     0x27
# Shield Ring     0x28
# Dork Ring     0x29
# Fin's Flute     0x2A
# Kael's Axe     0x2B
# Blood Axe     0x2C
# Dayblade     0x2D
# Shield Staff     0x2E
# Elf Cloak     0x2F
# Hawkblade     0x30
# Admt Sword     0x31
# Admt Shield     0x32
# Admt Dagger     0x33
# Admt Helm     0x34
# Admt Gloves     0x35
# Admt Mace     0x36
# Broom     0x37
# Pureblade     0x38
# Exorwand     0x39
# Ali's Carpet     0x3A
# Magic Mouth     0x3B
# Luckshield     0x3C
# Giant Fgn     0x3D
# Admt Chain     0x3E
# Admt Scale     0x3F
# Admt Plate     0x40
# Bracers [4]     0x41
# Arcshield     0x42
# Pure Shield     0x43
# Mage Staff     0x44
# War Staff     0x45
# Thief Dagger     0x46
# Soul Mace     0x47
# Wither Staff     0x48
# Sorcerstaff     0x49
# Sword of Pak     0x4A
# Heal Harp     0x4B
# Galt's Flute     0x4C
# Frost Horn     0x4D
# Dmnd Sword     0x4E
# Dmnd Shield     0x4F
# Dmnd Dagger     0x50
# Dmnd Helm     0x51
# Golem Fgn     0x52
# Titan Fgn     0x53
# Conjurstaff     0x54
# Arc's Hammer     0x55
# Staff of Lor     0x56
# Powerstaff     0x57
# Mournblade     0x58
# Dragonshield     0x59
# Dmnd Plate     0x5A
# Wargloves     0x5B
# Lorehelm     0x5C
# Dragonwand     0x5D
# Kiels Compass     0x5E
# Speedboots     0x5F
# Flame Horn     0x60
# Truthdrum     0x61
# Spiritdrum     0x62
# Pipes of Pan     0x63
# Ring of Power     0x64
# Deathring     0x65
# Ybarrashield     0x66
# Spectre Mace     0x67
# Dag Stone     0x68
# Arc's Eye     0x69
# Ogrewand     0x6A
# Spirithelm     0x6B
# Dragon Fgn     0x6C
# Mage Fgn     0x6D
# Troll Ring     0x6E
# Troll Staff     0x6F
# Onyx Key     0x70
# Crystal Sword     0x71
# Stoneblade     0x72
# Travelhelm     0x73
# Death Dagger     0x74
# Mongo Fgn     0x75
# Lich Fgn     0x76
# Eye     0x77
# Master Key     0x78
# WizWand     0x79
# Silvr Square     0x7A
# Silvr Circle     0x7B
# Silvr Triang     0x7C
# Thor Fgn     0x7D
# Old Man Fgn     0x7E
# Spectre Snare     0x7F


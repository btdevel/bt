from bt.extract.item_data import load_streets
bt_dir = '../content/msdos/Bard1'

class Street:
    def __init__(self, name=""):
        self.name = name
    def __str__(self):
        return self.name

class Building:
    def __init__(self, type, front=None):
        self.type = type
        self.front = front


class CityMap:
    def __init__(self, strmap, repl):
        self.map = [[repl.get(c, Street("???")) for c in line] for line in reversed(strmap)]

    def __getitem__(self, pt):
        try:
            return self.map[pt[1]][pt[0]]
        except:
            return None


def make_city_map():
    from bt.extract.huffman import read_city_name, read_city_path
    binmap = read_city_path()
    strmap = [binmap[i * 30:(i + 1) * 30] for i in xrange(30)]
    ustreet = Street("Unknown")
    repl = {0x00: ustreet,
            0x01: Building('house1'),
            0x02: Building('house2'),
            0x03: Building('house3'),
            0x04: Building('house4'),
            0x0B: Building('house3', 'guild.png'), # Adventurer's Guild
            0x12: Building('house2', 'pub.png'), # Pub/Inn
            0x1C: Building('house4', 'shop.png'), # Garth's Shop
            0x21: Building('house1', 'temple.png'), # Temple
            0x2B: "R", # Review Board
            0x60: Street("Statue here"), # Statue
            0x68: Street("Iron Gate"), # Gate to Tower
            0x71: Building('house1', 'temple.png'), # Catacombs/Mad God Temple
            0x78: Street("Sewer entrance"), # Stairs from Sewers
            0x81: Building('house2'), # Interplay Credits
            0x89: Building('house2'), # Roscoe's Energy Emporium
            0x91: Building('house1'), # Kylearan's Tower
            0x9B: Building('house1'), # Harkyn's Castle
            0xA1: Building('house1'), # Mangar's Tower
            0xA8: Street("City Gates"), # City Gates
            }

    nammap = read_city_name()
    streets = load_streets(bt_dir)
    cmap = CityMap(strmap, repl)
    for i in xrange(30):
        for j in xrange(30):
            if cmap[(i, j)] is ustreet:
                ind = nammap[i + (29 - j) * 30]
                if ind == 0xFF:
                    name = "Grand Plaz"
                elif ind < len(streets):
                    name = streets[ind]
                else:
                    name = "Unknown"

                cmap.map[j][i] = Street(name)
    return cmap

#
#   F2
# L2F1R2
# L1F0R1
# L0  R0

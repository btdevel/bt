import os
import pygame

from bt.extract.item_data import load_streets
from bt.movement import Direction, Vector
from bt.ui import EventHandler

class Street(object):
    def __init__(self, name=""):
        self.name = name
    def __str__(self):
        return self.name
    def is_building(self):
        return False

class Building(object):
    def __init__(self, type, front=None, action=None):
        self.type = type
        self.front = front
        self.action = action

    def is_building(self):
        return True

class CityMap(object):
    def __init__(self, strmap, repl):
        self.map = [[repl.get(c, Street("???")) for c in line] for line in reversed(strmap)]

    def __getitem__(self, pt):
        try:
            return self.map[pt[1]][pt[0]]
        except:
            return None

class CityUI(EventHandler):
    def __init__(self, map):
        EventHandler.__init__(self)
        self.map = map
        self.pos = Vector([25, 15])
        self.dir = Direction()

        self.add_key_event((pygame.K_UP, 0), self.forward)
        self.add_key_event((pygame.K_DOWN, 0), self.reverse)
        self.add_key_event((pygame.K_LEFT, 0), self.turn_left)
        self.add_key_event((pygame.K_RIGHT, 0), self.turn_right)
        self.add_key_event("?", self.print_location)

    def isbuildingat(self, forw, left=0):
        cell = self.map[self.pos +
                        forw * self.dir.forward_vec +
                        left * self.dir.left_vec]
        if cell.is_building():
            return cell
        return None


    def blit_building_at(self, state, forw, left=0):
        cell = self.isbuildingat(forw, left)
        if cell is None:
            return
        if forw == 1 and left == 0 and cell.front is not None:
            filename = cell.front
        else:
            base = 'FLR'[left] + str(forw - (left == 0))
            filename = os.path.join(cell.type, base + '.png')
        state.ui.blitim(filename)

    def redraw(self, state):
        s = state.ui.s
        if self.isbuildingat(1):
            pygame.draw.rect(s, pygame.Color(0, 0, 119),
                              pygame.Rect(33, 30, 224, 92 + 84))
        else:
            pygame.draw.rect(s, pygame.Color(0, 0, 119),
                              pygame.Rect(33, 30, 224, 92))
            pygame.draw.rect(s, pygame.Color(204, 119, 85),
                              pygame.Rect(33, 30 + 92, 224, 84))

        if self.isbuildingat(1):
            self.blit_building_at(state, 1)
        else:
            if self.isbuildingat(2):
                self.blit_building_at(state, 2)
            else:
                self.blit_building_at(state, 3)
                self.blit_building_at(state, 2, 1)
                self.blit_building_at(state, 2, -1)

            self.blit_building_at(state, 1, 1)
            self.blit_building_at(state, 1, -1)
            self.blit_building_at(state, 0, 1)
            self.blit_building_at(state, 0, -1)

        state.ui.update_display()


    def set_position(self, x, y):
        self.pos = Vector([x, y])

    def set_direction(self, dir):
        if not isinstance(dir, Direction):
            dir = Direction(dir)
        self.dir = dir


    def forward(self, state):
        cell = self.map[self.pos + self.dir.forward_vec]
        if not cell.is_building():
            self.pos = self.pos + self.dir.forward_vec
            self.redraw(state)
        else:
            state.set_current(cell.action, redraw=True)

    def reverse(self, state):
        self.dir.reverse()
        self.redraw(state)

    def turn_left(self, state):
        self.dir.left()
        self.redraw(state)

    def turn_right(self, state):
        self.dir.right()
        self.redraw(state)

    def print_location(self, state):
        state.ui.message("You are on %s facing %s." % (self.map[self.pos], str(self.dir)))


def make_city_map(btpath):
    import bt.buildings as bld

    from bt.extract.ext_levels import read_city_name, read_city_path
    binmap = read_city_path(btpath)
    strmap = [binmap[i * 30:(i + 1) * 30] for i in xrange(30)]
    ustreet = Street("Unknown")
    repl = {0x00: ustreet,
            0x01: Building('house1', action=bld.empty),
            0x02: Building('house2', action=bld.empty),
            0x03: Building('house3', action=bld.empty),
            0x04: Building('house4', action=bld.empty),
            0x0B: Building('house3', 'city/guild.png', action=bld.guild), # Adventurer's Guild
            0x12: Building('house2', 'city/pub.png', action=bld.pub), # Pub/Inn
            0x1C: Building('house4', 'city/shop.png', action=bld.shop), # Garth's Shop
            0x21: Building('house1', 'city/temple.png', action=bld.temple), # Temple
            0x2B: Building('house3', action=bld.review), # "R", # Review Board
            0x60: Street("Statue here"), # Statue
            0x68: Street("Iron Gate"), # Gate to Tower
            0x71: Building('house1', 'city/temple.png', action=bld.madgod), # Catacombs/Mad God Temple
            0x78: Street("Sewer entrance"), # Stairs from Sewers
            0x81: Building('house1', action=bld.credits), # Interplay Credits
            0x89: Building('house1', action=bld.roscoes), # Roscoe's Energy Emporium
            0x91: Building('house1', action=bld.kylearan), # Kylearan's Tower
            0x9B: Building('house1', action=bld.harkyn), # Harkyn's Castle *get front
            0xA1: Building('house1', action=bld.mangar), # Mangar's Tower
            0xA8: Street("City Gates"), # City Gates
            }

    nammap = read_city_name(btpath)
    streets = load_streets(btpath)
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

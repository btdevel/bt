import os
import pygame

from bt.extract.bt1.data import load_street_names
from bt.game.movement import Direction, Vector
from bt.game.ui import EventHandler

class ActionContainer(object):
    def __init__(self, action=None):
        if action is None:
            action = self.do_nothing
        self.action = action
    def do_nothing(self, state):
        pass
    def not_implemented(self, state):
        state.ui.message("This feature is not yet implemented.")


class Street(ActionContainer):
    def __init__(self, name="", action=None):
        ActionContainer.__init__(self, action)
        self.name = name
    def __str__(self):
        return self.name
    def is_building(self):
        return False

class Building(ActionContainer):
    def __init__(self, type, entry_handler, front=None):
        ActionContainer.__init__(self, self.enter_building)
        self.type = type
        self.front = front
        self.entry_handler = entry_handler
    def is_building(self):
        return True
    def enter_building(self, state):
        state.set_handler(self.entry_handler, redraw=True)

class CityMap(object):
    def __init__(self, strmap, repl):
        self.map = [[repl.get(c, Street("???")) for c in line] for line in reversed(strmap)]

    def __getitem__(self, pt):
        try:
            return self.map[pt[1]][pt[0]]
        except:
            return None

    def __setitem__(self, pt, item):
        self.map[pt[1]][pt[0]] = item

    def set_action(self, pt, action):
        import copy
        cell = copy.copy(self[pt])
        cell.action = action
        self[pt] = cell



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
        s = pygame.display.get_surface()
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


    def set_position(self, pos):
        self.pos = Vector(pos)

    def set_direction(self, dir):
        if not isinstance(dir, Direction):
            dir = Direction(dir)
        self.dir = dir


    def forward(self, state):
        cell = self.map[self.pos + self.dir.forward_vec]
        if not cell.is_building():
            self.pos = self.pos + self.dir.forward_vec
            self.redraw(state)
        cell.action(state)
#        else:
#            state.set_current(cell.action, redraw=True)

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
        state.ui.message(str(self.pos))


def make_city_map(btpath):
    import bt.game.buildings as bld

    from bt.extract.ext_levels import read_city_name, read_city_path
    binmap = read_city_path(btpath)
    strmap = [binmap[i * 30:(i + 1) * 30] for i in xrange(30)]
    ustreet = Street("Unknown")
    repl = {0x00: ustreet,
            0x01: Building('house1', bld.empty),
            0x02: Building('house2', bld.empty),
            0x03: Building('house3', bld.empty),
            0x04: Building('house4', bld.empty),
            0x0B: Building('house3', bld.guild, 'city/guild.png'), # Adventurer's Guild
            0x12: Building('house2', bld.pub, 'city/pub.png'), # Pub/Inn
            0x1C: Building('house4', bld.shop, 'city/shop.png'), # Garth's Shop
            0x21: Building('house1', bld.temple, 'city/temple.png'), # Temple
            0x2B: Building('house3', bld.review), # "R", # Review Board
            0x60: Street("Statue here"), # Statue
            0x68: Street("Iron Gate"), # Gate to Tower
            0x71: Building('house1', bld.madgod, 'city/temple.png'), # Catacombs/Mad God Temple
            0x78: Street("Sewer entrance"), # Stairs from Sewers
            0x81: Building('house1', bld.credits), # Interplay Credits
            0x89: Building('house1', bld.roscoes), # Roscoe's Energy Emporium
            0x91: Building('house1', bld.kylearan), # Kylearan's Tower
            0x9B: Building('house1', bld.harkyn), # Harkyn's Castle *get front
            0xA1: Building('house1', bld.mangar), # Mangar's Tower
            0xA8: Street("City Gates"), # City Gates
            }

    nammap = read_city_name(btpath)
    streets = load_street_names(btpath)
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

    def one_time_only_action(action):
        first = [True]
        def new_action(state):
            if first[0]:
                action(state)
                first[0] = False
        return new_action

    def message_action(msg):
        def message(state):
            state.ui.message(msg)
        return message

    def teleport_action(pos):
        def teleport(state):
            state.enter_city(pos=pos)
        return teleport

    def enter_action(handler):
        def execute(state):
            state.set_handler(handler, redraw=True)
        return execute


    cmap.set_action([25, 18], message_action("Garth shop is to the right"))
    cmap.set_action([25, 16], one_time_only_action(message_action("the shoppe is ahead")))
    cmap.set_action([25, 3], teleport_action([25, 6]))

    cmap.set_action([27, 25], enter_action(bld.iron_gate))
    cmap.set_action([27, 6], enter_action(bld.statue))

    return cmap

#
#   F2
# L2F1R2
# L1F0R1
# L0  R0

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
        return "Street(%s)" % self.name
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
    def __str__(self):
        return "Building(%s,%s)" % (self.type, self.front)

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
        if cell is not None and cell.is_building():
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

        # naming for building images with location relative to xx  
        #    F2
        # L2 F1 R2
        # L1 F0 R1
        # L0 xx R0
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
        with state.ui.message_pane.noupdate():
            cell = self.map[self.pos + self.dir.forward_vec]
            state.ui.clear_message()
        
            if not cell.is_building():
                self.pos = self.pos + self.dir.forward_vec
                self.redraw(state)
                self.print_location(state)
        cell.action(state)

    def reverse(self, state):
        self.dir.reverse()
        self.redraw(state)
        state.ui.clear_message()

    def turn_left(self, state):
        self.dir.left()
        self.redraw(state)
        state.ui.clear_message()

    def turn_right(self, state):
        self.dir.right()
        self.redraw(state)
        state.ui.clear_message()

    def print_location(self, state):
        print 1
        state.ui.clear_message(update=False)
        print 2
        state.ui.message("You are on %s facing %s." % (self.map[self.pos].name, str(self.dir)), update=False)
        print 3
        state.ui.message("\n\nYou are on: %dE, %dN" % tuple(self.pos))
        print 4


class Array2d(object):
    def __init__(self, w, h, data=None):
        self.w = w
        self.h = h
        if data is None:
            self.data = [None] * w * h
        else:
            assert len(data) == w * h
            self.data = data
    def _index(self, pt):
        return (self.h - 1 - pt[1]) * self.w + pt[0]

    def __getitem__(self, pt):
        if pt[0] < 0 or pt[0] >= self.w or pt[1] < 0 or pt[1] >= self.h:
            return None
        return self.data[self._index(pt)]

    def __setitem__(self, pt, item):
        self.data[self._index(pt)] = item

    def set_action(self, pt, action):
        import copy
        cell = copy.copy(self[pt])
        cell.action = action
        self[pt] = cell


def make_city_map_new(btpath):
    import bt.game.buildings as bld
    import bt.game.action as action

    from bt.extract.ext_levels import read_city_name, read_city_path

    patmap = Array2d(30, 30, read_city_path(btpath))
    nammap = Array2d(30, 30, read_city_name(btpath))
    streets = load_street_names(btpath)
    cmap = Array2d(30, 30)

    for i in xrange(30):
        for j in xrange(30):
            type = patmap[(i, j)] & 7
            special = patmap[(i, j)] >> 3
            nameind = nammap[(i, j)]

            if type == 0:
                curr = Street(streets[nameind])
                if special == 12:
                    curr.action = action.enter(bld.statue)
                elif special == 13:
                    if j < 15:
                        curr.action = action.enter(bld.iron_gate_mangar)
                    else:
                        curr.action = action.enter(bld.iron_gate_kylearan)
                elif special == 15:
                    curr.action = action.message("Entrance to sewers here")
                elif special == 21:
                    curr.action = action.enter(bld.city_gate)
                elif special == 0:
                    pass
                else:
                    print "Unknown street special:" + str(special)
            else:
                curr = Building('house' + str(type), None)
                if special == 0: # normal house
                    curr.entry_handler = bld.empty
                elif special == 1: # Adventurer's Guild
                    curr.entry_handler = bld.guild
                    curr.front = 'city/guild.png'
                elif special == 2: # Pub/Inn
                    curr.entry_handler = bld.pub
                    curr.front = 'city/pub.png'
                elif special == 3: # Garth's Shop
                    curr.entry_handler = bld.shop
                    curr.front = 'city/shop.png'
                elif special == 4: # Temple
                    curr.entry_handler = bld.temple
                    curr.front = 'city/temple.png'
                elif special == 5: # "R", # Review Board
                    curr.entry_handler = bld.review
                elif special == 14: # Catacombs/Mad God Temple
                    curr.entry_handler = bld.madgod
                    curr.front = 'city/temple.png'
                elif special == 16: # Interplay Credits
                    curr.entry_handler = bld.credits
                elif special == 17: # Roscoe's Energy Emporium
                    curr.entry_handler = bld.roscoes
                elif special == 18: # Kylearan's Tower
                    curr.entry_handler = bld.kylearan
                elif special == 19: # Harkyn's Castle *get front
                    curr.entry_handler = bld.harkyn
                    curr.front = 'city/castle.png'
                elif special == 20: # Mangar's Tower
                    curr.entry_handler = bld.mangar
                else:
                    print "Unknown building special:" + str(special)
            cmap[(i, j)] = curr

#    cmap.set_action([25, 18], action.message("Garth shop is to the right"))
#    cmap.set_action([25, 16], action.one_time_only(action.message("The shoppe is ahead")))
    cmap.set_action([25, 2], action.teleport([25, 7]))
    cmap[4, 16].entry_handler = bld.stable
    cmap[4, 15].entry_handler = bld.stable
    return cmap

make_city_map = make_city_map_new


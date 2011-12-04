import os
import pygame

from bt.game.movement import Direction, Vector
from bt.game.ui import EventHandler
from bt.game.app import app

class Cell(object):
    def __init__(self, action=None):
        self.action = action


class Street(Cell):
    def __init__(self, name="", action=None):
        Cell.__init__(self, action)
        self.name = name
    def __str__(self):
        return "Street(%s)" % self.name
    def is_building(self):
        return False

class Building(Cell):
    def __init__(self, type, entry_handler, front=None):
        Cell.__init__(self, self.enter_building)
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



class CityHandler(EventHandler):
    def __init__(self, map, location=""):
        EventHandler.__init__(self, location=location)
        self.map = map
        self.pos = Vector([0, 0])
        self.dir = Direction()

        self.show_pos = app.config.debug.show_pos(default=False, type=bool)

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
        state.ui.blit_image(filename)

    def redraw(self, state):
        with state.ui.world_view.noupdate():
            surf = state.ui.world_view.get_surf()
            if self.isbuildingat(1):
                pygame.draw.rect(surf, pygame.Color(0, 0, 119),
                                 pygame.Rect(0, 0, 224, 92 + 84))
            else:
                pygame.draw.rect(surf, pygame.Color(0, 0, 119),
                                 pygame.Rect(0, 0, 224, 92))
                pygame.draw.rect(surf, pygame.Color(204, 119, 85),
                                 pygame.Rect(0, 0 + 92, 224, 84))

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


    def set_position(self, pos):
        self.pos = Vector(pos)

    def set_direction(self, dir):
        if not isinstance(dir, Direction):
            dir = Direction(dir)
        self.dir = dir


    def forward(self, state):
        with state.ui.message_view.noupdate():
            cell = self.map[self.pos + self.dir.forward_vec]
            state.ui.clear_message()

            if not cell.is_building():
                self.pos = self.pos + self.dir.forward_vec
                self.redraw(state)
                if self.show_pos:
                    self.print_location(state)
        if cell.action:
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
        with state.ui.message_view.noupdate() as msg:
            msg.clear()
            msg.message("You are on %s facing %s." % (self.map[self.pos].name, str(self.dir)))
            msg.message("\n\nYou are on: %dE, %dN" % tuple(self.pos))


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



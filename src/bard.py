dir = '../res'
bt_dir = '../content/msdos/Bard1'

from pygame import Surface
import pygame
import os, sys, glob


from bt.movement import *
from bt.city import *
from bt.ui import *

ui = UI(dir)
ui.init()
s = ui.s

class State: pass
state = State()
state.ui = ui

def isbuildingat(state, forw, left=0):
    cell = state.map[state.pos +
                     forw * state.dir.forward_vec +
                     left * state.dir.left_vec]
    if isinstance(cell, Building):
        return cell
    return None

def blitim(file, type=type):
    im = pygame.image.load(os.path.join(dir, file))
    s.blit(im, (33, 30))

def blit_building_at(state, forw, left=0):
    cell = isbuildingat(state, forw, left)
    if cell is None:
        return
    if forw == 1 and left == 0 and cell.front is not None:
        file = cell.front
    else:
        base = 'FLR'[left] + str(forw - (left == 0))
        file = os.path.join(cell.type, base + '.png')
    im = pygame.image.load(os.path.join(dir, file))
    s.blit(im, (33, 30))



def redraw(state):
    print state.map[state.pos]
    if isbuildingat(state, 1):
        pygame.draw.rect(s, pygame.Color(0, 0, 119),
                          pygame.Rect(33, 30, 224, 92 + 84))
    else:
        pygame.draw.rect(s, pygame.Color(0, 0, 119),
                          pygame.Rect(33, 30, 224, 92))
        pygame.draw.rect(s, pygame.Color(204, 119, 85),
                          pygame.Rect(33, 30 + 92, 224, 84))

    if isbuildingat(state, 1):
        blit_building_at(state, 1)
    else:
        if isbuildingat(state, 2):
            blit_building_at(state, 2)
        else:
            blit_building_at(state, 3)
            blit_building_at(state, 2, 1)
            blit_building_at(state, 2, -1)

        blit_building_at(state, 1, 1)
        blit_building_at(state, 1, -1)
        blit_building_at(state, 0, 1)
        blit_building_at(state, 0, -1)

    pygame.display.flip()

def forward(state):
    if not isinstance(state.map[state.pos + state.dir.forward_vec], Building):
        state.pos = state.pos + state.dir.forward_vec
        redraw(state)
    else:
        pass #enter building

def reverse(state):
    state.dir.reverse()
    redraw(state)

def turn_left(state):
    state.dir.left()
    redraw(state)

def turn_right(state):
    state.dir.right()
    redraw(state)

def exit(state):
    state.running = False

def nop(state):
    pass

#state.map = CityMap(strmap, repl)
state.map = make_city_map()
state.dir = Direction()
state.pos = Vector([25, 15])
state.running = True
redraw(state)

pygame.time.set_timer(pygame.USEREVENT + 1, 300)

keymap = {}
keymap[(pygame.K_UP, 0)] = forward
keymap[(pygame.K_DOWN, 0)] = reverse
keymap[(pygame.K_LEFT, 0)] = turn_left
keymap[(pygame.K_RIGHT, 0)] = turn_right
keymap[(pygame.K_q, pygame.KMOD_LCTRL)] = exit

while state.running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            pass
        elif event.type == pygame.KEYUP:
            keymap.get((event.key, event.mod), nop)(state)
            #print event
        elif event.type == pygame.QUIT:
            exit(state)
        else:
            #print event 
            pass

ui.quit()

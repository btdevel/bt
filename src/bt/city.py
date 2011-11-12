# coding=UTF8

import numpy as np

strmap=[
    #012345678901234567890123456789
    u"██████████████████████████████",
    u"███                     ██   █",
    u"██  ███████ █████ █████    █ █",
    u"██        █ █   █      █ █   █",
    u"█  ███  █ █ █ █   ████ █ ██ ██",
    u"█  ██     █ █          █ ██ ██",
    u"██ ███  ███ ████ ███  ██ ██ ██",
    u"██     █       █     █       █",
    u"█      █ ██ ██  ████ █ ██ ████",
    u"█ ████ █  █   █    █ █ ██ █ ██",
    u"█    █    ███ ████   █ ██    █",
    u"█ ██ ████  ██ ████████ █  S ██",
    u"█ █      █ ██        █ █     █",
    u"███ █ ██ ████     ██ █ ██ 4███",
    u"█   █ ██   ██     ██   █G ████",
    u"███ █   ██ ██     ████ ██ ████",
    u"█ █ ███  █        ████ █     █",
    u"█ █    █ ████████ █  █ █  ████",
    u"█   ██ █   ██████ █     █    █",
    u"█      █ █   ██   █ ███  ██ ██",
    u"███ ██ █  ██ ██ ███    █ ██  █",
    u"███ ██ █  ██       █  ██  █ ██",
    u"█    █ █  █████████████ █ █  █",
    u"███ ██ █     ██    ███  █ █ ██",
    u"██  █  █  ██    ██      █ █ ██",
    u"██ ███ █  ██████       ██ █ ██",
    u"█   █  █          █  █  █ █ ██",
    u"█ █   ███████████       █ █  █",
    u"█   ██████████████████  █ ████",
    u"█████████████████████████ ████"
  ]

strmap=[
    #012345678901234567890123456789
    u"██████████████████████████████",
    u"███                     ██   █",
    u"██  ███████ █████ █████    █ █",
    u"██        █ █   █      █ █   █",
    u"█  ███  █ █ █ █   ████ █ ██ ██",
    u"█  ██     █ █          █ ██ ██",
    u"██ ███  ███ ████ ███  ██ ██ ██",
    u"██     █       █     █       █",
    u"█      █ ██ ██  ████ █ ██ ████",
    u"█ ████ █  █   █    █ █ ██ █ ██",
    u"█    █    ███ ████   █ ██    █",
    u"█ ██ ████  ██ ████████ █  S ██",
    u"█ █      █ ██        █ █     █",
    u"███ █ ██ ████     ██ █ █4 4███",
    u"█   █ ██   ██     ██   █G 1███",
    u"███ █   ██ ██     ████ █2 213█",
    u"█ █ ███  █        ████ 2     2",
    u"█ █    █ ████████ █  █ 1  124█",
    u"█   ██ █   ██████ █     4    2",
    u"█      █ █   ██   █ ███  32 3█",
    u"███ ██ █  ██ ██ ███    █ █T  3",
    u"███ ██ █  ██       █  ██  3 4█",
    u"█    █ █  █████████████ █ 1  1",
    u"███ ██ █     ██    ███  █ 2 1█",
    u"██  █  █  ██    ██      █ 1 P█",
    u"██ ███ █  ██████       ██ 4 3█",
    u"█   █  █          █  █  █ 3 1█",
    u"█ █   ███████████       █ 1  3",
    u"█   ██████████████████  █ █43█",
    u"█████████████████████████ ████"
  ]

class Street:
    def __init__(self, name=""):
        self.name = name
    def __str__(self):
        return self.name

class Building:
    def __init__(self, type, front=None):
        self.type = type
        self.front = front

repl = {u" ": Street("Unknown"), 
        u"█": Building('house1'), 
        u"1": Building('house1'), 
        u"2": Building('house2'), 
        u"3": Building('house3'), 
        u"4": Building('house4'), 
        u"G": Building('house3', 'guild.png'), 
        u"S": Building('house4', 'shop.png'), 
        u"T": Building('house1', 'temple.png'), 
        u"P": Building('house2', 'pub.png')
        }

class CityMap:
    def __init__(self, strmap, repl):
        self.map = [[repl[c] for c in line] for line in reversed(strmap)]
    def __getitem__(self, pt):
        try:
            return self.map[pt[1]][pt[0]]
        except:
            return None


_left = lambda dir: (dir + 1) % 4
_reverse = lambda dir: (dir + 2) % 4
_right = lambda dir: (dir + 3) % 4
class Direction():
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3
    vectors = np.array([[0, 1], [-1, 0], [0, -1], [1, 0]])

    def __init__(self, dir=NORTH):
        self.dir = dir

    def left(self):
        self.dir = _left(self.dir)

    def reverse(self):
        self.dir = _reverse(self.dir)

    def right(self):
        self.dir = _right(self.dir)
    
    @property
    def forward_vec(self):
        return Direction.vectors[self.dir,:]
    @property
    def left_vec(self):
        return Direction.vectors[_left(self.dir),:]
    @property
    def right_vec(self):
        return Direction.vectors[_right(self.dir),:]
        
#
#   F2
# L2F1R2
# L1F0R1
# L0  R0

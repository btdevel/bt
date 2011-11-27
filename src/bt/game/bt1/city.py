from bt.extract.bt1.data import load_street_names
from bt.extract.ext_levels import read_city_name, read_city_path

from bt.game.app import app
from bt.game.city import (CityHandler, Array2d, Street, Building)
import bt.game.buildings as bld
import bt.game.action as action


def make_city_map(btpath):
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
#                    curr.action = None
                elif special == 15:
                    curr.action = action.enter(bld.sewers_entrance)
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

def get_city_handler():
    btpath = app.config.msdos_path()
    return CityHandler(make_city_map(btpath), location="Skara Brae")

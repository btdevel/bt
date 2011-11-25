import pygame
from bt.game.ui import EventHandler
import bt.game.action as action

from bt.game.handler import DefaultBuildingHandler, ImageDisplayHandler

class EmptyBuildingHandler(DefaultBuildingHandler):
    def __init__(self, filename, message):
        DefaultBuildingHandler.__init__(self, filename, message)

    def key_event(self, state, key):
        if EventHandler.key_event(self, state, key):
            return True
        action.exit_building()(state)
        return True

empty = EmptyBuildingHandler("inside/empty.png", "You're in an empty building.")

stable = EmptyBuildingHandler("inside/empty.png", "Sorry, friends, all the horses have been eaten by creatures!")




from bt.game.bt1.credits import credits
from bt.game.bt1.guild import guild
from bt.game.bt1.castle import harkyn
from bt.game.bt1.review import review
from bt.game.bt1.shop import shop
from bt.game.bt1.tavern import pub
from bt.game.bt1.temple import madgod, temple




roscoes = DefaultBuildingHandler("inside/roscoes.png", """Welcome, my friends, to Roscoe's Energy Emporium. 
Who needeth spell points restored?""")
#Roscoe's
#restoration.
# has some definite spell point problems. It will cost 
#Roscoe re-energizes him.


kylearan = DefaultBuildingHandler("inside/empty.png", """This is the entry chamber to Kylearan's Amber Tower. 
A stairwell leads up to a lofty level of chambers.
You can:

Take stairs""")
#Amber Tower

mangar = DefaultBuildingHandler("inside/empty.png", """This is the entry chamber to Mangar's Tower. 
A stairwell leads up to the first level of traps and terrors. 
You can:

Take stairs""")
#Magic mouth
#A magic mouth on the wall speaks to you: "Despised 
#ones, none save Mangar may enter his demesne."
#The Tower


class TurnBackHandler(DefaultBuildingHandler):
    def __init__(self, filename, message, display=""):
        DefaultBuildingHandler.__init__(self, filename, message, exit_action=action.turn_back())

class IronGateHandler(TurnBackHandler):
    def __init__(self, filename, message, display=""):
        DefaultBuildingHandler.__init__(self, filename, message, exit_action=action.turn_back())

class GuardianHandler(EventHandler):
    def __init__(self, filename, message, display=None):
        EventHandler.__init__(self)
        self.add_key_event("lL", action.turn_back())
        self.add_key_event("aA", action.compose(action.enter_city(), action.message("The statue gives up...")))
        self.filename = filename
        self.message = message

    def redraw(self, state):
        state.ui.clear_view()
        state.ui.blitim(self.filename)
        state.ui.update_display()
        # this should go into some "enter" method
        state.ui.clear_message()
        state.ui.message(self.message)


statue = GuardianHandler("city/statue.png", """You stand before a gate, which is guarded by the statue of a %{statue}. You can:

Attack it.
Leave it.""", display="Guardian")


iron_gate_mangar = IronGateHandler("city/gate.png", "You stand before an iron gate, beyond which stands Mangar's tower.", display="Iron Gate")
iron_gate_kylearan = IronGateHandler("city/gate.png", "You stand before an iron gate, beyond which stands Kylearan's tower.", display="Iron Gate")

city_gate = TurnBackHandler("city/city_gate.png", "You stand before the city gates, which are blocked by a gigantic snow drift.", display="")




from bt.game.handler import EventHandler, DefaultBuildingHandler, MultiScreenHandler, Screen
import bt.game.action as action
from bt.game.app import app

class EmptyBuildingHandler(DefaultBuildingHandler):
    def __init__(self, filename, message, location=""):
        DefaultBuildingHandler.__init__(self, filename, message, location=location)

    def key_event(self, state, key):
        if EventHandler.key_event(self, state, key):
            return True
        action.exit_building()(state)
        return True

empty = EmptyBuildingHandler("inside/empty.png", "You're in an empty building.")
empty.location = "Empty building"

stable = EmptyBuildingHandler("inside/empty.png", "Sorry, friends, all the horses have been eaten by creatures!")
stable.location = "Empty building"




from bt.game.bt1.credits import credits
from bt.game.bt1.guild import guild
from bt.game.bt1.castle import harkyn
from bt.game.bt1.review import review
from bt.game.bt1.shop import shop
from bt.game.bt1.tavern import pub
from bt.game.bt1.temple import temple
from bt.game.bt1.madgod import madgod
from bt.game.bt1.mangar import mangar
from bt.game.bt1.kylearan import kylearan
from bt.game.bt1.castle import harkyn
from bt.game.bt1.roscoes import roscoes


class TurnBackHandler(DefaultBuildingHandler):
    def __init__(self, filename, message, location=""):
        DefaultBuildingHandler.__init__(self, filename, message, exit_action=action.turn_back(), location=location)

class GuardianHandler(EventHandler):
    def __init__(self, filename, message, location=""):
        EventHandler.__init__(self, location=location)
        self.add_key_event("lL", action.turn_back())
        self.add_key_event("aA", action.compose(action.enter_city(), action.message("The statue gives up...")))
        self.filename = filename
        self.message = message

    def redraw(self, state):
        state.ui.clear_view()
        state.ui.blit_image(self.filename)
        state.ui.update_display()
        # this should go into some "enter" method
        app.values["statue"] = "Stone Golem"
        app.values["statue"] = "Blue Dragon"
        app.values["statue"] = "Ogre Magician"
        app.values["statue"] = "Samurai"
        state.ui.clear_message()
        state.ui.message(self.message)


statue = GuardianHandler("city/statue.png", """\nYou stand before a gate, which is guarded by the statue of a %(statue)s. You can:


Attack it.
Leave it.""", location="Guardian")

class IronGateHandler(TurnBackHandler):
    def __init__(self, filename, message, location=""):
        DefaultBuildingHandler.__init__(self, filename, message, exit_action=action.turn_back(), location=location)

iron_gate_mangar = IronGateHandler("city/gate.png", "You stand before an iron gate, beyond which stands Mangar's tower.", location="Iron Gate")
iron_gate_kylearan = IronGateHandler("city/gate.png", "You stand before an iron gate, beyond which stands Kylearan's tower.", location="Iron Gate")


city_gate = TurnBackHandler("city/city_gate.png", "You stand before the city gates, which are blocked by a gigantic snow drift.", location="City Gate")

app.values["charname"] = "DESMET IRKM"





# Entrance to sewers
class SewersEntryHandler(MultiScreenHandler):
    pass

sewers_entrance = SewersEntryHandler(None, location="Portal...")

screen = Screen()
screen.add_message("There is an entrance to the city sewers here. Do you wish to take it?\n ")
screen.add_option('Yes', 'yY', action.turn_back())
screen.add_option('No', 'nN', action.turn_back())
sewers_entrance.add_screen("main", screen)



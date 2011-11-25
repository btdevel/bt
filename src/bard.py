from bt.game.city import CityUI, make_city_map
from bt.game.buildings import guild
from bt.game.ui import UI
from bt.game.app import app

app.read_config(["bt1-game.conf"])

class State:
    def __init__(self):
        self.ui = UI(app.config["path"]["images"])
        self.city_handler = CityUI(make_city_map(app.config["path"]["msdos"]))
        self.curr_handler = guild

    def run(self):
        self.ui.init()
        self.ui.event_loop(self)

    def set_handler(self, curr, redraw=True):
        self.curr_handler = curr
        self.ui.redraw()

    def redraw(self):
        self.ui.redraw()

State().run()

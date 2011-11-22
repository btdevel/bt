from bt.game.city import CityUI, make_city_map
from bt.game.buildings import guild
from bt.game.ui import UI

res_path = '../res/image/bt1'
bt_path = '../res/msdos/bt1'

class State:
    def __init__(self):
        self.ui = UI(res_path)
        self.city_handler = CityUI(make_city_map(bt_path))
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

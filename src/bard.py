from bt.city import CityUI, make_city_map
from bt.buildings import guild
from bt.ui import UI

res_path = '../res/image'
bt_path = '../content/msdos/Bard1'

class State:
    def __init__(self):
        self.ui = UI(res_path)
        self.map = CityUI(make_city_map(bt_path))
        self.current = guild

    def run(self):
        self.ui.init()
        self.ui.event_loop(self)

    def set_current(self, curr, redraw=True):
        self.current = curr
        self.ui.redraw()

State().run()

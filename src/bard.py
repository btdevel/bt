from bt.game.app import app
app.read_config(["bt1-game.conf"])

from bt.game.bt1.city import get_city_handler
from bt.game.buildings import guild
from bt.game.character import Party
from bt.game.ui import UI


class State:
    def __init__(self):
        self.ui = UI()
        self.city_handler = get_city_handler()
        self.curr_handler = None
        self.party = Party()

    def run(self):
        self.ui.init(self)
        self.set_handler(guild, True)
        self.ui.event_loop()

    def set_handler(self, curr, redraw=True):
        self.curr_handler = curr
        self.ui.show_location(curr.location)
        self.ui.redraw()

    def redraw(self):
        self.ui.redraw()

    def message_view_ctx(self):
        return self.ui.message_view.noupdate()

State().run()

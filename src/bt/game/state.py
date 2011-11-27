from bt.game.character import Party
from bt.game.ui import UI

class State:
    def __init__(self, city_handler, start_handler):
        self.city_handler = city_handler
        self.start_handler = start_handler
        self.curr_handler = None
        self.ui = UI()
        self.party = Party()

    def run(self):
        self.ui.init(self)
        self.set_handler(self.start_handler, True)
        self.ui.event_loop()

    def set_handler(self, curr, redraw=True):
        if self.curr_handler:
            self.curr_handler.exit(self)
        self.curr_handler = curr
        self.curr_handler.enter(self)
        self.ui.show_location(curr.location)
        self.redraw()

    def redraw(self):
        self.ui.redraw()

    def message_view_ctx(self):
        return self.ui.message_view.noupdate()

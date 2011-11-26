def one_time_only(action):
    first = [True]
    def new_action(state):
        if first[0]:
            action(state)
            first[0] = False
    return new_action

def compose(*actions):
    def execute(state):
        for action in actions:
            action(state)
    return execute

def message(msg):
    def execute(state):
        state.ui.message(msg)
    return execute

def teleport(pos):
    def execute(state):
        state.city_handler.set_position(pos)
        state.redraw()
    return execute

def enter(handler):
    def execute(state):
        state.set_handler(handler, redraw=True)
    return execute

def enter_city(pos=None, newdir=None):
    def execute(state):
        if pos is not None:
            state.city_handler.set_position(pos)
        if newdir is not None:
            state.city_handler.set_direction(newdir)
        state.set_handler(state.city_handler, redraw=True)
    return execute

def exit_building():
    def execute(state):
        state.city_handler.reverse(state)
        state.set_handler(state.city_handler, redraw=True)
    return execute

def turn_back():
    def execute(state):
        state.city_handler.reverse(state)
        state.city_handler.forward(state)
        state.set_handler(state.city_handler, redraw=True)
    return execute

def change_screen(name):
    def execute(state):
        state.curr_handler.set_screen(state, name)
    return execute

def leave_game():
    def execute(state):
        state.running = False
    return execute

def do_nothing():
    def execute(state):
        pass
    return execute

def add_member(filename):
    def execute(state):
        state.party.add(filename)
    return execute

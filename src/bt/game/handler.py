import pygame
import bt.game.action as action

class EventHandler(object):
    def __init__(self, location=""):
        self.keymap = {}
        self.location = location
    def enter(self, state):
        pass
    def exit(self, state):
        pass
    def add_key_event(self, key, action):
        if isinstance(key, str):
            for c in key:
                self.keymap[c] = action
        else:
            self.keymap[key] = action
    def key_event(self, state, key):
        if key in self.keymap:
            self.keymap[key](state)
            return True
        return False

class ImageDisplayHandler(EventHandler):
    def __init__(self, filename, location=""):
        EventHandler.__init__(self, location=location)
        self.filename = filename
    def redraw(self, state):
        state.ui.clear_view()
        if self.filename:
            state.ui.blit_image(self.filename)
        else:
            state.city_handler.redraw(state)


class DefaultBuildingHandler(ImageDisplayHandler):
    def __init__(self, filename, message, exit_action=action.exit_building(), location=""):
        ImageDisplayHandler.__init__(self, filename, location=location)
        self.add_key_event((pygame.K_ESCAPE, 0), exit_action)
        self.add_key_event("eE", exit_action)
        self.message = message

    def redraw(self, state):
        # this should go into some "enter" method
        ImageDisplayHandler.redraw(self, state)
        with state.message_view_ctx() as msg:
            msg.clear()
            msg.message(self.message)
            msg.message("(EXIT)", pos= -1, center=True)

class MultiScreenHandler(ImageDisplayHandler):
    def __init__(self, filename, location=""):
        ImageDisplayHandler.__init__(self, filename, location=location)
        self.screens = {}
        self.current = None
        self.start = None

    def add_screen(self, name, screen):
        if self.start is None:
            self.start = name
        assert name not in self.screens
        self.screens[name] = screen
        screen.set_parent(self)

    def enter(self, state):
        self.set_screen(state, self.start)

    def exit(self, state):
        if self.current:
            self.current.exit(state)

    def set_screen(self, state, name):
        if self.current:
            self.current.exit(state)
        state.ui.message_view.clear()
        self.current = self.screens[name]
        self.current.enter(state)
        self.current.redraw(state)
    def key_event(self, state, key):
        return self.current.key_event(state, key)
    def redraw(self, state):
        ImageDisplayHandler.redraw(self, state)
        state.ui.message_view.clear()
        self.current.redraw(state)


class Screen(EventHandler):
    def __init__(self):
        EventHandler.__init__(self)
        self.messages = []
        self.parent = None

    def set_parent(self, parent):
        assert self.parent is None
        self.parent = parent

    def clear(self):
        self.messages = []
        self.keymap = {}

    def add_message(self, text, pos=None, center=False):
        self.messages.append((text, pos, center))

    def add_option(self, text, keys, action, pos=None, center=False):
        self.add_message(text, pos=pos, center=center)
        self.add_key_event(keys, action)

    def redraw(self, state):
        with state.ui.message_view.noupdate() as view:
            for text, pos, center in self.messages:
                view.message(text, pos=pos, center=center)

def continue_screen(msg, action=None, target=None):
    import bt.game.action as btaction
    if action is None:
        action = btaction.change_screen(target)

    screen = Screen()
    screen.add_message(msg)
    screen.add_option('          (CONTINUE)', 'cC', action, pos= -1)
    return screen


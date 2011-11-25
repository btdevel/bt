import pygame
import bt.game.action as action

class EventHandler(object):
    def __init__(self):
        self.keymap = {}
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
    def __init__(self, filename):
        EventHandler.__init__(self)
        self.filename = filename
    def redraw(self, state):
        state.ui.clear_view()
        state.ui.blitim(self.filename)
        state.ui.update_display()

class DefaultBuildingHandler(ImageDisplayHandler):
    def __init__(self, filename, message, exit_action=action.exit_building()):
        ImageDisplayHandler.__init__(self, filename)
        self.add_key_event((pygame.K_ESCAPE, 0), exit_action)
        self.add_key_event("eE", exit_action)
        self.message = message

    def redraw(self, state):
        # this should go into some "enter" method
        ImageDisplayHandler.redraw(self, state)
        with state.message_view_ctx() as msg:
            msg.clear()
            msg.message(self.message)
            msg.message("     (EXIT)")
        print "building message printed"

class MultiScreenHandler(ImageDisplayHandler):
    def __init__(self, filename):
        ImageDisplayHandler.__init__(self, filename)
        self.screens = {}
        self.current = None

    def add_screen(self, name, screen):
        if self.current is None:
            self.current = screen
        self.screens[name] = screen
        screen.set_parent(self)
    def set_screen(self, state, name):
        state.ui.message_pane.clear()
        self.current = self.screens[name]
        self.current.redraw(state)
    def key_event(self, state, key):
        return self.current.key_event(state, key)
    def redraw(self, state):
        ImageDisplayHandler.redraw(self, state)
        state.ui.message_pane.clear()
        self.current.redraw(state)


class Screen(EventHandler):
    def __init__(self):
        EventHandler.__init__(self)
        self.msg = ""
        self.parent = None
    def set_parent(self, parent):
        assert self.parent is None
        self.parent = parent

    def add_message(self, text):
        if self.msg == "":
            self.msg = text
        else:
            self.msg += "\n" + text
    def add_option(self, text, keys, action):
        self.add_message(text)
        self.add_key_event(keys, action)
    def redraw(self, state):
        state.ui.message_pane.message(self.msg)

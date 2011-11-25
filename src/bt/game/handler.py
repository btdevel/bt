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

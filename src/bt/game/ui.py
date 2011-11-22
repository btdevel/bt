import pygame
import os

import bt.game.messages as messages

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



class UI(EventHandler):
    def __init__(self, resdir):
        EventHandler.__init__(self)
        self.resdir = resdir
        self.add_key_event((pygame.K_q, pygame.KMOD_LCTRL), self.request_exit)
        self.message_pane = messages.MessagePane(pygame.Rect(340, 30, 264, 198))


    def init(self):
        pygame.display.init()
        pygame.font.init()

        pygame.display.set_mode((640, 400))
        pygame.key.set_repeat(200, 200)

        s = pygame.display.get_surface()
        main = pygame.image.load(os.path.join(self.resdir, 'main.png'))
        s.blit(main, (0, 0))
        pygame.display.flip()

    def request_exit(self, state):
        state.running = False

    def cleanup(self):
        pygame.quit()

    def redraw(self):
        self.message_pane.clear()
        self.state.curr_handler.redraw(self.state)

    def blitim(self, filename):
        s = pygame.display.get_surface()
        im = pygame.image.load(os.path.join(self.resdir, filename))
        s.blit(im, (33, 30))

    def update_display(self):
        pygame.display.flip()

    def event_loop(self, state):
        self.state = state
        state.running = True
        self.redraw()

        pygame.time.set_timer(pygame.USEREVENT + 1, 300)
        while state.running:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    pass
                elif event.type == pygame.KEYDOWN:
                    key = (event.key, event.mod)
                    used = state.curr_handler.key_event(state, key)
                    if not used and hasattr(event, "unicode"):
                        used = state.curr_handler.key_event(state, event.unicode)
                    if not used:
                        used = self.key_event(state, key)
                    if not used and hasattr(event, "unicode"):
                        used = self.key_event(state, event.unicode)
                    if not used and False:
                        print event
                elif event.type == pygame.QUIT:
                    self.request_exit(state)
                else:
                    #print event 
                    pass

        self.cleanup()


    def clear_message(self):
        self.message_pane.clear()

    def clear_view(self):
        s = pygame.display.get_surface()
        pygame.draw.rect(s, pygame.Color(0, 0, 119),
                            pygame.Rect(33, 30, 224, 92 + 84))
        # no update        

    def message(self, msg):
        self.message_pane.message(msg)

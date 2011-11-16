'''
Created on 12.11.2011

@author: ezander
'''
import pygame
import os

class EventHandler(object):
    def __init__(self):
        self.keymap = {}
    def add_key_event(self, key, action):
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

    def init(self):
        pygame.display.init()
        pygame.display.set_mode((640, 480))
        s = pygame.display.get_surface()
        main = pygame.image.load(os.path.join(self.resdir, 'main.png'))
        s.blit(main, (0, 0))
        pygame.display.flip()
        self.s = s

    def request_exit(self, state):
        state.running = False

    def cleanup(self):
        pygame.quit()

    def redraw(self):
        self.state.current.redraw(self.state)

    def blitim(self, filename):
        im = pygame.image.load(os.path.join(self.resdir, filename))
        self.s.blit(im, (33, 30))

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
                    used = state.current.key_event(state, key)
                    if not used and hasattr(event, "unicode"):
                        used = state.current.key_event(state, event.unicode)
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

    def message(self, text, clear=True):
        # clear is ignored for now
        print(text)

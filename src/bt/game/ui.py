import pygame
import os

import bt.game.view as view
import bt.game.charview as charview
from bt.game.handler import EventHandler
from bt.game.app import app


class UI(EventHandler):
    def __init__(self):
        EventHandler.__init__(self)
        self.add_key_event((pygame.K_q, pygame.KMOD_LCTRL), self.request_exit)

        self.image_path = app.config.main.image_path()

        self.message_view = view.View(pygame.Rect(340, 30, 264, 198), config=app.config.message_view)
        self.world_view = view.View(pygame.Rect(34, 30, 222, 176), config=app.config.world_view)
        self.location_view = view.View(pygame.Rect(34, 207, 222, 25), config=app.config.location_view)

        self.use_own_headings = app.config.character_view.use_own_headings(default=True, type=bool)
        if self.use_own_headings:
            char_rect = pygame.Rect(30, 242, 578, 110)
        else:
            char_rect = pygame.Rect(30, 266, 578, 110)
        self.char_view = charview.CharacterView(char_rect, config=app.config.character_view)

    def init(self, state):
        self.state = state
        pygame.display.init()
        pygame.font.init()

        pygame.display.set_mode((640, 400))
        pygame.key.set_repeat(200, 200)

        surf = pygame.display.get_surface()
        main = pygame.image.load(os.path.join(self.image_path, 'main.png'))
        surf.blit(main, (0, 0))

        self.message_view.clear()
        self.world_view.clear()
        self.location_view.clear()
        self.char_view.clear()

        pygame.display.flip()

    def request_exit(self, state):
        state.running = False

    def cleanup(self):
        pygame.quit()

    def redraw(self):
        self.message_view.clear()
        self.state.curr_handler.redraw(self.state)
        self.char_view.redraw(self.state)

    def event_loop(self):
        state = self.state
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

    def blit_image(self, filename):
        self.world_view.blit_image(filename)

    def update_display(self):
        self.world_view.update()

    def clear_view(self):
        self.world_view.clear()

    def clear_message(self):
        self.message_view.clear()

    def message(self, msg):
        self.message_view.message(msg)

    def show_location(self, location):
        with self.location_view.noupdate() as view:
            view.clear()
            view.print_centered(location)

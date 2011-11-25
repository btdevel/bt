import pygame

from bt.game.app import app

def split_into_lines(text, width_ok_func):
    for par in text.split("\n"):
        words = par.split(" ") + [""]
        ind = 0
        while ind < len(words) - 1:
            line = ""
            while width_ok_func(line) and ind < len(words):
                oldline = line
                line = line + " " + words[ind]
                ind += 1
            yield oldline[1:]
            ind -= 1


class MessagePane():
    def __init__(self, rect):
        view_config = app.config.message_view
        self.fgcolor = view_config.fgcolor(default=(0, 0, 0), type=pygame.Color)
        self.bgcolor = view_config.bgcolor(default=(255, 255, 255), type=pygame.Color)
        self.sidesep = view_config.sidesep(default=0, type=int)
        self.topsep = view_config.topsep(default=0, type=int)
        self.linesep = view_config.linesep(default=0, type=int)
        self.smooth = view_config.smooth(default=False, type=bool)
        self.delay = view_config.delay(default=10, type=int)

        self.scrrect = rect.inflate(-2 * self.sidesep, -2 * self.topsep)
        self.rect = self.scrrect.move(-self.scrrect.left, -self.scrrect.top)
        self.pos = self.rect.topleft

        font_config = view_config.font
        self.fontfilename = font_config.filename()
        self.fontsize = font_config.fontsize(14, type=int)
        self.update_flag = True

        self.font = None
        self.surf = None

    def get_font(self):
        if not self.font:
            if not self.fontfilename:
                self.fontfilename = pygame.font.get_default_font()
            self.font = pygame.font.Font(self.fontfilename, self.fontsize)
        return self.font

    def get_surf(self):
        if not self.surf:
            surf = pygame.display.get_surface()
            self.surf = surf.subsurface(self.scrrect)
        return self.surf


    def clear(self, update=True):
        print "clearing"
        surf = self.get_surf()
        pygame.draw.rect(surf, self.bgcolor, self.rect)
        self.pos = self.rect.topleft
        self.update(update)

    def update(self, update=True):
        if update and self.update_flag:
            print "... updating"
            pygame.display.update(self.scrrect)

    def noupdate(self):
        class UpdateCtx(object):
            def __init__(self, mp):
                self.mp = mp
            def __enter__(self):
                self.old_flag = self.mp.update_flag
                self.mp.update_flag = False
                return self.mp
            def __exit__(self, *args):
                self.mp.update_flag = self.old_flag
                self.mp.update(True)
        return UpdateCtx(self)

    def _scroll_up(self, surf, y, dy, ds):
        surf = self.get_surf()
        if hasattr(surf, "scroll"):
            surf.scroll(0, -ds)
        y -= ds
        dy = self.rect.bottom - y
        rect = self.rect.move(0, 0)
        rect.top = y
        rect.height = dy
        pygame.draw.rect(surf, self.bgcolor, rect)
        return y, dy



    def message(self, msg, update=True):
        surf = self.get_surf()
        font = self.get_font()

        def width_ok(line):
            return font.size(line)[0] < self.rect.width

        x, y = self.pos
        for line in split_into_lines(msg, width_ok):
                im = font.render(line, 1, self.fgcolor)
                dy = font.size(line)[1] + self.linesep
                if not line:
                    dy /= 2 # empty lines are only half size
                scroll = y + dy > self.rect.bottom
                if scroll:
                    ds = (y + dy) - self.rect.bottom
                    if self.smooth and update:
                        for i in xrange(ds):
                            y, dy = self._scroll_up(surf, y, dy, 1)
                            pygame.time.delay(self.delay)
                            self.update(update)
                    else:
                        y, dy = self._scroll_up(surf, y, dy, ds)
                        pygame.time.delay(ds * self.delay)
                        self.update(update)
                surf.blit(im, (x, y))
                self.update(update and scroll)
                y += dy
        self.pos = x, y
        self.update(update)

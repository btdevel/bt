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
            yield oldline
            ind -= 1


class MessagePane():
    def __init__(self, rect, bgcolor=(255, 255, 255)):
        self.outer = rect.move(0, 0)
        self.bgcolor = bgcolor
        self.sidesep = 6
        self.topsep = 4
        self.linesep = 0
        self.rect = rect.inflate(-self.sidesep, -self.topsep)
        self.pos = self.rect.topleft
        self.fgcolor = (0, 0, 0)
        self.smooth = True
        self.delay = 25
        self.font = None

        font_config = app.config["font"]
        self.fontfilename = font_config["filename"]
        self.fontsize = int(font_config.get("fontsize", 14))
        self.update_flag=True

    def clear(self, update=True):
        print "clearing"
        s = pygame.display.get_surface()
        pygame.draw.rect(s, self.bgcolor, self.rect)
        self.pos = self.rect.topleft
        self.update(update)

    def update(self, update=True):
        if update and self.update_flag:
            print "... updating"
            pygame.display.update(self.rect)

    def noupdate(self):
        class UpdateCtx(object):
            def __init__(self, mp): 
                self.mp=mp
            def __enter__(self): 
                self.old_flag = self.mp.update_flag
                self.mp.update_flag = False
            def __exit__(self, *args): 
                self.mp.update_flag = self.old_flag
                self.mp.update(True)
        return UpdateCtx(self)

    def _scroll_up(self, surf, y, dy, ds):
        sub = surf.subsurface(self.rect)
        if hasattr(sub, "scroll"):
            sub.scroll(0, -ds)
        y -= ds
        dy = self.rect.bottom - y
        rect = self.rect.move(0, 0)
        rect.top = y
        rect.height = dy
        pygame.draw.rect(surf, self.bgcolor, rect)
        return y, dy


    def _get_font(self):
        if self.font:
            return self.font
        if self.fontfilename is None:
            self.fontfilename = pygame.font.get_default_font()
        self.font = pygame.font.Font(self.fontfilename, self.fontsize)
        return self.font

    def message(self, msg, update=True):
        surf = pygame.display.get_surface()
        font = self._get_font()

        def width_ok(line):
            return font.size(line)[0] < self.rect.width

        x, y = self.pos
        for line in split_into_lines(msg, width_ok):
                im = font.render(line, 1, self.fgcolor)

                dy = font.size(line)[1] + self.linesep
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
        

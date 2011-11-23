import pygame

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
        self.outer = rect.move(0,0)
        self.bgcolor = bgcolor
        self.sidesep = 6
        self.topsep = 4
        self.linesep = -7
        self.rect = rect.inflate(-self.sidesep, -self.topsep)
        self.pos = self.rect.topleft
        self.fgcolor = (60, 20, 20)
        self.fontname = None
        self.fontsize = 14
        self.smooth = True
        self.delay = 25
        self.font = None

    def clear(self):
        s = pygame.display.get_surface()
        pygame.draw.rect(s, self.bgcolor, self.rect)
        self.pos = self.rect.topleft



    def _scroll_up(self, surf, y, dy, ds):
        sub = surf.subsurface(self.rect)
        sub.scroll(0, -ds)
        y -= ds
        dy = self.rect.bottom - y
        rect = self.rect.copy()
        rect.top = y
        rect.height = dy
        pygame.draw.rect(surf, self.bgcolor, rect)
        return y, dy


    def _get_font(self):
        if self.font:
            return self.font
        if self.fontname is None:
            fontname = pygame.font.get_default_font()
        else:
            fontname = pygame.font.match_font(self.fontname)
        self.font = pygame.font.Font(fontname, self.fontsize)
        return self.font

    def message(self, msg):
        surf = pygame.display.get_surface()
        font = self._get_font()

        def width_ok(line):
            return font.size(line)[0] < self.rect.width

        x, y = self.pos
        for line in split_into_lines(msg, width_ok):
                im = font.render(line, 1, self.fgcolor)

                dy = font.size(line)[1] + self.linesep
                if y + dy > self.rect.bottom:
                    ds = (y + dy) - self.rect.bottom
                    if self.smooth:
                        for i in xrange(ds):
                            y, dy = self._scroll_up(surf, y, dy, 1)
                            pygame.time.delay(self.delay)
                            pygame.display.update(self.rect)
                    else:
                        y, dy = self._scroll_up(surf, y, dy, ds)
                        pygame.time.delay(ds * self.delay)
                        pygame.display.update(self.rect)
                surf.blit(im, (x, y))
                pygame.display.update(self.rect)
                y += dy
        self.pos = x, y
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
        self.fgcolor = (0, 0, 0)
        self.fontname = None
        self.fontsize = 14
        self.smooth = True
        self.delay = 25
        self.font = None

        pygame.font.init()
        fontfilename = "/home/ezander/Downloads/btdist/res/font/COMMOD64.TTF"

        fontfilename = "/home/ezander/Downloads/btdist/res/font/CBM-6420.TTF"
        self.fontsize = 12
        self.linesep = 0

        fontfilename = "/home/ezander/Downloads/btdist/res/font/CBM-64.TTF"
        self.fontsize = 14
        self.linesep = 0

        fontfilename = "/home/ezander/Downloads/btdist/res/font/CBM-6480.TTF"
        self.fontsize = 20
        self.linesep = 0

        fontfilename = "/home/ezander/Downloads/btdist/res/font/c64.ttf"
        self.fontsize = 14
        self.linesep = 0
        self.font = pygame.font.Font(fontfilename, self.fontsize)
        self.foo = 1

        self.update_flag=True

    def clear(self, update=True):
        print "clearing", self.foo
        self.foo += 1
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
        rect = self.rect.move(0,0)
        rect.top = y
        rect.height = dy
        pygame.draw.rect(surf, self.bgcolor, rect)
        return y, dy


    def _get_font(self):
        if self.font:
            return self.font
        if self.fontname is None:
            fontfilename = pygame.font.get_default_font()
        else:
            fontfilename = pygame.font.match_font(self.fontname)
        self.font = pygame.font.Font(fontfilename, self.fontsize)
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
        

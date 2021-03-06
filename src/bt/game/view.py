import os
import pygame

from bt.game.app import app, Config

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

class View():
    def __init__(self, rect, config=Config()):
        self.fgcolor = config.fgcolor(default=(0, 0, 0), type=pygame.Color)
        self.bgcolor = config.bgcolor(default=(255, 255, 255), type=pygame.Color)
        self.sidesep = config.sidesep(default=0, type=int)
        self.topsep = config.topsep(default=0, type=int)
        self.linesep = config.linesep(default=0, type=int)
        self.smooth = config.smooth(default=False, type=bool)
        self.delay = config.delay(default=10, type=int)
        self.image_path = config.image_path()
        self.diffx = config.diffx(default=0, type=int)

        self.scrrect = rect.inflate(-2 * self.sidesep, -2 * self.topsep)
        self.rect = self.scrrect.move(-self.scrrect.left, -self.scrrect.top)
        self.pos = self.rect.topleft

        font_config = config.font
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


    def clear(self):
        surf = self.get_surf()
        pygame.draw.rect(surf, self.bgcolor, self.rect)
        self.pos = self.rect.topleft
        self.update()

    def update(self):
        if self.update_flag:
#            print "... updating"
            pygame.display.update(self.scrrect)

    def blit_image(self, filename, pos=(0, 0)):
        surf = self.get_surf()
        im = pygame.image.load(os.path.join(self.image_path, filename))
        if self.diffx:
            pos = (pos[0] - self.diffx, pos[1])
        surf.blit(im, pos)
        self.update()

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
                self.mp.update()
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

    def _interpolate_string(self, text):
        try:
            text = text % app.values
        except ValueError:
            print "ValueError in " + text
        return text

    def print_centered(self, text):
        surf = self.get_surf()
        font = self.get_font()
        text = self._interpolate_string(text)
        im = font.render(text, 1, self.fgcolor)
        x = self.rect.left + (self.rect.width - im.get_width()) // 2
        y = self.rect.top + (self.rect.height - im.get_height()) // 2
        surf.blit(im, (x, y))
        self.update()

    def print_list_entry(self, text, reversed=False):
        surf = self.get_surf()
        font = self.get_font()
        text = self._interpolate_string(text)
        if not reversed:
            im = font.render(text, 1, self.fgcolor)
        else:
            im = font.render(text, 1, 
                             pygame.Color("#000033"), 
                             pygame.Color("#FFFF77"))
        x, y = self.pos
        surf.blit(im, (x, y))
        y += font.size(text)[1] + self.linesep
        self.pos = (x,y)
        self.update()

    def print_tabbed(self, texts, tabs):
        surf = self.get_surf()
        font = self.get_font()
        x, y = self.pos

        if isinstance(texts, str):
            texts = texts.split("\t")

        for i, text in  enumerate(texts):
            text = self._interpolate_string(text)
            im = font.render(text, 1, self.fgcolor)
            if i < len(tabs):
                x, mode = tabs[i]
            else:
                print "Not enough tabs %d/%d" % (len(texts), len(tabs))
                # reuse last value
            if mode in 'rR':
                x -= im.get_width()
            elif mode in 'cC':
                x -= im.get_width() // 2

            surf.blit(im, (x, y))
            x += im.get_width() + im.get_height() // 2
            self.update()
        self.pos = self.rect.left, y + im.get_height() + self.linesep
        self.update()

    def message(self, msg, update=True, pos=None, center=False):
        surf = self.get_surf()
        font = self.get_font()


        def width_ok(line):
            return font.size(line)[0] < self.rect.width

        x, y = self.pos
        if pos is not None:
            y = self.rect.bottom + pos * (self.fontsize + self.linesep)

        msg = self._interpolate_string(msg)
        for line in split_into_lines(msg, width_ok):
                im = font.render(line, 1, self.fgcolor)
                if center:
                    x = self.rect.left + (self.rect.width - im.get_width()) // 2
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
                            self.update()
                    else:
                        y, dy = self._scroll_up(surf, y, dy, ds)
                        pygame.time.delay(ds * self.delay)
                surf.blit(im, (x, y))
                self.update()
                y += dy
        self.pos = self.rect.left, y
        self.update()

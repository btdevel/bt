from bt.game.handler import EventHandler
from bt.game.view import View
import bt.game.character

class CharacterView(View):
    def redraw(self, state):
        party = state.party

        with self.noupdate() as view:
            view.clear()
            if state.ui.use_own_headings:
                # use own tabs   
                tabs = ((0, "L"), (280, "R"), (360, "R"), (440, "R"), 
                        (520, "R"), (536, "L"))
                view.print_tabbed("Character Name\tAC\tHits\tCnd\tSpSt\tCl", tabs)
            else:
                # use tabs for the original amiga screen   
                tabs = ((0, "L"), (286, "R"), (366, "R"), (446, "R"), 
                        (526, "R"), (544, "L"))

            for char in party.chars:
                char.ac = "10"
                #FIXME: need to compute AC
                attribs = "%s\t%s\t%s\t%s\t%s\t%s" % (char.name, char.ac, char.max_hp, char.curr_hp, char.curr_sp, char.char_class)
                view.print_tabbed(attribs, tabs)


class CharDisplayHandler(EventHandler):
    def __init__(self):
        EventHandler.__init__(self)
        #self.add_key_event

chardisp = ["inside/empty.png",
                             """N %(char_name)s
Race: %(char_race)s
Class: %(char_class)s
St: %(char_st)2d IQ: %(char_iq)2d  
Dx: %(char_dx)2d Cn: %(char_cn)2d
Lk: %(char_lk)2d HP: %(char_hp)2d
Lvl: %(char_level)2d HP: %(char_sppt)d
Exper: %(char_exp)d
Gold:  %(char_gold)d
(POOL GOLD)
(TRADE GOLD)
(CONTINUE)"""]

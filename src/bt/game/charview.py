import bt.game.view as view
import bt.game.character

class CharacterView(view.View):
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

            print party.chars
            for char in party.chars:
                char.ac = "10"
                attribs = "%s\t%s\t%s\t%s\t%s\t%s" % (char.name, char.ac, char.max_hp, char.curr_hp, char.curr_sp, char.char_class)
                view.print_tabbed(attribs, tabs)


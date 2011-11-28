import bt.game.action as action
from bt.game.handler import (MultiScreenHandler, Screen, continue_screen)
from bt.game.movement import Direction
from bt.game.bt1.char import (get_char_list, load_msdos_char)


class GuildHandler(MultiScreenHandler):
    pass

guild = GuildHandler("inside/guild.png", location="The guild")

# The main screen
screen = Screen()
screen.add_message("Thou art in the Guild of Adventurers.\n ")
screen.add_option('Add member', 'aA', action.change_screen("add_member"))
screen.add_option('Remove member', 'rR', action.change_screen("remove_member"))
screen.add_option('Create a member', 'cC', action.change_screen("create_member"))
screen.add_option('Delete a member', 'dD', action.change_screen("delete_member"))
screen.add_option('Save party', 'sS', action.change_screen("save_party"))
screen.add_option('Leave game', 'lL', action.change_screen("leave_game"))
screen.add_option('Enter the city', 'eE',
#                  action.enter_city(pos=[2, 3], newdir=Direction.NORTH))
                  action.enter_city(pos=[25, 15], newdir=Direction.NORTH))
guild.add_screen("main", screen)
del screen

# The leave Game screen
screen = Screen()
screen.set_cancel_screen("main")
screen.add_message("Leave game?\n ")
screen.add_option('Yes', 'yY', action.leave_game())
screen.add_option('No', 'nN', action.change_screen("main"))
guild.add_screen("leave_game", screen)

# The "Add member" screen (and helpers)
def add_member(character):
    def execute(state):
        ret = state.party.add(character)
        if ret:
            screens = [None, "already_in_party", "no_room"]
            action.change_screen(screens[ret])(state)
            return
        state.ui.char_view.redraw(state)
        action.change_screen("main")
    return execute


class AddMemberScreen(Screen):
    def enter(self, state):
        if state.party.is_full():
            action.change_screen("roster_full")(state)
            return

        self.clear()
        for i, char in enumerate(get_char_list()):
            if char.is_party:
                line = "*"
            else:
                line = "  "
            line += char.name
            line = str(i) + " " + line
            rchar = load_msdos_char(char.filename)
            self.add_option(line, "%d" % i, add_member(rchar))
            if i == 9:
                break
        self.set_cancel_screen("main")

guild.add_screen("add_member", AddMemberScreen())


# Remove member screen
def remove_member(number):
    def execute(state):
        char = state.party.remove(number)
        # FIXME: char must be saved also
        state.ui.char_view.redraw(state)
        action.change_screen("main")
    return execute

class RemoveMemberScreen(Screen):
    def enter(self, state):
        self.clear()
        if state.party.is_empty():
            self.add_message("\nWhat party!")
            self.add_option("\n(CONTINUE)", "cC", action.change_screen("main"), pos= -1, center=True)
        else:
            self.add_message("\nPick the party member to save to disk and remove from the party.")
            for i in range(len(state.party.chars)):
                self.add_key_event(chr(ord("1") + i), remove_member(i))
            self.add_option("\n(CANCEL)", "cC", action.change_screen("main"), pos= -1, center=True)
        self.set_cancel_screen("main")
    pass
guild.add_screen("remove_member", RemoveMemberScreen())

# Some short message screens
def message_screen(msg):
    return continue_screen("\n\n%s" % msg, target="main")


guild.add_screen("roster_full",
                 message_screen("Sorry, the roster is full."))

guild.add_screen("no_room",
                 message_screen("No room to add new members."))

guild.add_screen("already_in_party",
                 message_screen("That member is already in the party."))

guild.add_screen("what_party",
                 message_screen("What party!"))

guild.add_screen("must_have_party",
                 message_screen("You must have a party to enter the city."))


# Not yet implemented screens
def not_implemented():
    return continue_screen("\nNot implemented yet.", target="main")

guild.add_screen("create_member", not_implemented())
guild.add_screen("delete_member", not_implemented())
guild.add_screen("save_party", not_implemented())



#Name to save party under?
#That name is already in use.
#Do you still want to use it?
#Error trying to read in 
#Select a race for your new character:
#    (REROLL)
#Enter the new member's name.
#You can't delete a member in your party from the disk.
#This will permanently remove 
# from the disk! Do you wish to do this?
#File not found.
#error trying to save member in slot 
#. name not found in name table!
#Error on write.
#error on party write.
#Error on creating party file.
#Error on read.
#Error trying to find 
#Sorry, I got a disk error trying to read him in.

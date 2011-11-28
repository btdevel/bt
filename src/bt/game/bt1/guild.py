import bt.game.action as action
from bt.game.handler import MultiScreenHandler, Screen, continue_screen
from bt.game.movement import Direction

class GuildHandler(MultiScreenHandler):
    pass

guild = GuildHandler("inside/guild.png", location="The guild")

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

screen = Screen()
screen.add_message("Leave game?\n ")
screen.add_option('Yes', 'yY', action.leave_game())
screen.add_option('No', 'nN', action.change_screen("main"))
guild.add_screen("leave_game", screen)


from bt.game.bt1.char import (get_char_list, load_msdos_char)

def add_member(character):
    def execute(state):
        ret = state.party.add(character)
        print ret, not ret[0]
        if not ret[0]:
            action.change_screen(ret[1])(state)
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
        import pygame
        self.add_key_event((pygame.K_ESCAPE, 0), action.change_screen("main"))

guild.add_screen("add_member", AddMemberScreen())





def not_implemented():
    return continue_screen("\nNot implemented yet.", target="main")

def roster_full():
    return continue_screen("\nSorry, the roster is full.", target="main")

def what_party():
    return continue_screen("\nWhat party!", target="main")

def already_in_party():
    return continue_screen("\nThat member is already in the party.", target="main")
guild.add_screen("already_in_party", already_in_party())
guild.add_screen("roster_full", roster_full())

#


guild.add_screen("remove_member", what_party())
guild.add_screen("create_member", not_implemented())
guild.add_screen("delete_member", not_implemented())
guild.add_screen("save_party", what_party())



#
#
#Name to save party under?
#That name is already in use.
#Do you still want to use it?
#Leave the game?
#You must have a party to enter the city.
#The guild
#The guild
#No room to add new members.
#Error trying to read in 
#What party!
#Pick the party member to save to disk and remove from the party.
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

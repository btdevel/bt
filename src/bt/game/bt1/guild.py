import pygame

import bt.game.action as action
from bt.game.handler import (MultiScreenHandler, Screen, continue_screen)
from bt.game.movement import Direction
from bt.game.app import app


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
def add_member(char):
    def execute(state):
        if char.is_party:
            char_loader = app.get_char_loader()
            # FIXME: check if char exists, do with loop, return when full
            ret = state.party.add(char_loader.load_char_by_name(char.name1))
            ret = state.party.add(char_loader.load_char_by_name(char.name2))
            ret = state.party.add(char_loader.load_char_by_name(char.name3))
            ret = state.party.add(char_loader.load_char_by_name(char.name4))
            ret = state.party.add(char_loader.load_char_by_name(char.name5))
            ret = state.party.add(char_loader.load_char_by_name(char.name6))
        else:
            ret = state.party.add(char)
            if ret:
                screens = [None, "already_in_party", "no_room"]
                action.change_screen(screens[ret])(state)
                return
        state.ui.char_view.redraw(state)
        action.change_screen("main")
    return execute


class AddMemberScreen(Screen):
    def make_char_list(self):
        char_loader = app.get_char_loader()
        list = []
        for i, charinfo in enumerate(char_loader.char_list()):
            if charinfo.is_party:
                line = "*"
            else:
                line = "  "
            line += charinfo.name
            char = char_loader.load_char(charinfo.filename)
            list.append((i, line, char))
        return list

    def newenter(self, state):
        if state.party.is_full():
            action.change_screen("roster_full")(state)
            return

        self.clear()
        self.list = self.make_char_list()
        self.start_disp=0
        self.num_disp=10
        self.num_sel=0
        self.set_cancel_screen("main")
        self.add_key_event( (pygame.K_DOWN, 0), self.down )
        self.add_key_event( (pygame.K_UP, 0), self.up )
        self.add_key_event( (pygame.K_RETURN, 0), self.select )

    def enter(self, state):
        return self.newenter(state)

    def redraw(self, state):
        with state.ui.message_view.noupdate() as view:
            view.clear()
            if self.list:
                for i in xrange(self.start_disp,self.start_disp+self.num_disp):
                    if i>=len(self.list):
                        break
                    line = self.list[i][1]
                    view.print_list_entry(line+"  ", i==self.num_sel)
            else:
                for text, pos, center in self.messages:
                    view.message(text, pos=pos, center=center)

    def up(self, state):
        if self.num_sel>0:
            self.num_sel-=1
        if self.num_sel<self.start_disp:
            self.start_disp-=1
        self.redraw(state)

    def down(self, state):
        if self.num_sel<len(self.list)-1:
            self.num_sel+=1
        if self.num_sel>=self.start_disp+self.num_disp:
            self.start_disp+=1
        self.redraw(state)

    def select(self, state):
        print self.list[self.num_sel]
        add_member(self.list[self.num_sel][2])(state)

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
#Select a race for your new character:
#    (REROLL)
#Enter the new member's name.
#That name is already in use.
#Do you still want to use it?


guild.add_screen("delete_member", not_implemented())
#You can't delete a member in your party from the disk.
#This will permanently remove 
# from the disk! Do you wish to do this?


guild.add_screen("save_party", not_implemented())
#Name to save party under?
#That name is already in use.
#Do you still want to use it?





# Error messages (unused currently)
#====================================
#Error trying to read in 
#File not found.
#error trying to save member in slot 
#. name not found in name table!
#Error on write.
#error on party write.
#Error on creating party file.
#Error on read.
#Error trying to find 
#Sorry, I got a disk error trying to read him in.

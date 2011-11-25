import pygame
import bt.game.action as action
from bt.game.handler import ImageDisplayHandler, DefaultBuildingHandler

class GuildHandler(DefaultBuildingHandler):
    def __init__(self, filename, message):
        from bt.game.movement import Direction
        DefaultBuildingHandler.__init__(self, filename, message)
        self.add_key_event("aA", self.add_member)
        self.add_key_event("rR", self.remove_member)
        self.add_key_event("cC", self.create_member)
        self.add_key_event("dD", self.delete_member)
        self.add_key_event("sS", self.save_party)
        self.add_key_event("lL", self.leave_game)
        self.add_key_event("eE", action.enter_city(pos=[25, 15], newdir=Direction.NORTH))

    def add_member(self, state):
        state.ui.message("Not implemented yet.")

    def remove_member(self, state):
        state.ui.message("Not implemented yet.")

    def create_member(self, state):
        state.ui.message("Not implemented yet.")

    def delete_member(self, state):
        state.ui.message("Not implemented yet.")

    def save_party(self, state):
        state.ui.message("Not implemented yet.")

    def leave_game(self, state):
        state.running = False



guild = GuildHandler("inside/guild.png", """Thou art in the Guild of Adventurers.

Add member
Remove member
Create a member
Delete a member
Save party
Leave game
Enter the city
""")
#Sorry, the roster is full.
#What party!
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
#Sorry, the roster is full.
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
#That member is already in the party.
#error on party write.
#Error on creating party file.
#Error on read.
#Error trying to find 
#Sorry, I got a disk error trying to read him in.

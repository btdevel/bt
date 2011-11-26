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



def not_implemented():
    return continue_screen("\nNot implemented yet.", target="main")

def roster_full():
    return continue_screen("\nSorry, the roster is full.", target="main")

def what_party():
    return continue_screen("\nWhat party!", target="main")

guild.add_screen("add_member", not_implemented())
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

import pygame
import bt.game.action as action
from bt.game.handler import MultiScreenHandler, Screen

class TavernHandler(MultiScreenHandler):
    pass

tavern = TavernHandler("inside/pub.png", location="Tavern")
pub = tavern

tavern_greeting_screen = Screen()
tavern_greeting_screen.add_message("Hail, travelers! Step to the bar and I'll draw you a tankard.")
tavern_greeting_screen.add_message("\nYou can:\n")
tavern_greeting_screen.add_option('Order a drink', 'oO', action.change_screen("order"))
tavern_greeting_screen.add_option('Talk to barkeep', 'tT', action.change_screen("talk"))
tavern_greeting_screen.add_message("\n\n\n")
tavern_greeting_screen.add_option('(EXIT)', 'eE', action.exit_building(), pos= -1, center=True)

tavern_order_screen = Screen()
tavern_order_screen.add_message("Seat thyself, %(charname)s. We've got...\n")
tavern_order_screen.add_option("Ale", "aA", action.message("Not bad!!"))
tavern_order_screen.add_option("Beer", "bB", action.message("Not bad!!"))
tavern_order_screen.add_option("Mead", "mM", action.message("Not bad!!"))
tavern_order_screen.add_option("Foul spirits", "fF", action.message("You don't feel too well."))
tavern_order_screen.add_option("Ginger Ale", "gG", action.message("The girls in the tavern are not impressed."))
tavern_order_screen.add_option("Wine", "wW", action.message("The barkeep says, \"Go down to the cellar and pick out a bottle.\""))
tavern_order_screen.add_message("\n\nWhat'll it be?")
tavern_order_screen.add_option('(CANCEL)', 'cC', action.change_screen("greeting"), pos= -1, center=True)

tavern_talk_screen = Screen()
tavern_talk_screen.add_message("\"Talk ain't cheap,\" the barkeep says.")
tavern_talk_screen.add_message("\nHow much will you tip him?\n\n\n")
tavern_talk_screen.add_option('(CANCEL)', 'cC', action.change_screen("greeting"), pos= -1, center=True)




tavern.add_screen("greeting", tavern_greeting_screen)
#tavern.add_screen("whodrinks", tavern_who_drinks_screen)
tavern.add_screen("order", tavern_order_screen)
tavern.add_screen("talk", tavern_talk_screen)
#tavern.add_screen("tip", tavern_tip_screen)


#'Who will drink?
#Seat thyself, 
#. We've got...
#Beer
#Mead
#Foul spirits
#Ginger Ale
#Wine
#What'll it be?

def tip_message(value):
    if value == 0:
        return None
    elif value < 200:
        return '"The guardians can be deadly," the barkeep smirks.'
    elif value < 300:
        return '"A taste of wine might turn to ready adventure," the barkeep chuckles.'
    elif value < 400:
        return '"Look for the Review Board on Trumpet Street," the barkeep whispers.'
    elif value < 500 or value >= 700:
        return '"The gates cannot be scaled, but an entrance always exists," the barkeep stutters.'
    else:
        return '"The Stone Golem has been spoken of twofold," the barkeep smiles.'


#You don't feel too well.
#The girls in the tavern are not impressed.
#The barkeep says, "Go down to the cellar and pick out a bottle."
#Not bad!!
#Who will talk to the barkeep?
#"Talk ain't cheap," the barkeep says.
#How much will you tip him?
#"Money talks, buddy," he says.
#Scarlet Bard
#Sinister Inn
#Dragonbreath
#Ask Y'Mother
#Archmage Inn
#Skull Tavern
#Drawnblade
#Tavern

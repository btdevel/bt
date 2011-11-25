import pygame
import bt.game.action as action
from bt.game.handler import MultiScreenHandler, Screen

pub = MultiScreenHandler("inside/pub.png")

pub_greeting_screen = Screen()
pub_greeting_screen.add_message("Hail, travelers! Step to the bar and I'll draw you a tankard.")
pub_greeting_screen.add_message("\nYou can:")
pub_greeting_screen.add_option('Order a drink', 'oO', action.change_screen("order"))
pub_greeting_screen.add_option('Talk to barkeep', 'tT', action.change_screen("talk"))
pub_greeting_screen.add_message("\n\n\n")
pub_greeting_screen.add_option('      (EXIT)', 'eE', action.exit_building())

pub_order_screen = Screen()
pub_order_screen.add_message("Seat thyself, %{charname}. We've got...")
pub_order_screen.add_option("Beer", "bB", action.message("Not bad!!"))
pub_order_screen.add_option("Mead", "mM", action.message("Not bad!!"))
pub_order_screen.add_option("Foul spirits", "fF", action.message("You don't feel too well."))
pub_order_screen.add_option("Ginger Ale", "gG", action.message("The girls in the tavern are not impressed."))
pub_order_screen.add_option("Wine", "wW", action.message("The barkeep says, \"Go down to the cellar and pick out a bottle.\""))
pub_order_screen.add_message("\nWhat'll it be?")
pub_order_screen.add_option('      (CANCEL)', 'cC', action.change_screen("greeting"))

pub_talk_screen = Screen()
pub_talk_screen.add_message("\"Talk ain't cheap,\" the barkeep says.")
pub_talk_screen.add_message("\nHow much will you tip him?\n\n\n")
pub_talk_screen.add_option('      (CANCEL)', 'cC', action.change_screen("greeting"))




pub.add_screen("greeting", pub_greeting_screen)
#pub.add_screen("whodrinks", pub_who_drinks_screen)
pub.add_screen("order", pub_order_screen)
pub.add_screen("talk", pub_talk_screen)
#pub.add_screen("tip", pub_tip_screen)


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

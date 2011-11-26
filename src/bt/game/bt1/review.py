import bt.game.action as action
from bt.game.handler import MultiScreenHandler, Screen, continue_screen
from bt.game.movement import Direction

class ReviewHandler(MultiScreenHandler):
    pass

review = ReviewHandler("inside/review.png", location="Review board")

screen = Screen()
screen.add_message("Wouldst thou like to be reviewed for:\n ")
screen.add_option('Advancement', 'aA', action.change_screen("advancement"))
screen.add_option('Spell Acquiring', 'sS', action.change_screen("spell_acquiring"))
screen.add_option('Class Change', 'cC', action.change_screen("class_change"))
screen.add_option('(EXIT)', 'eE', action.turn_back(), pos= -1, center=True)
review.add_screen("main", screen)

def not_implemented():
    return continue_screen("\nNot implemented yet.", target="main")

review.add_screen("advancement", not_implemented())
review.add_screen("spell_acquiring", not_implemented())
review.add_screen("class_change", not_implemented())


#The review Board is closed for the evening. The guild 
#leaders will meet with you in the morning.
#
#Who seeks knowledge of the mystic arts?
#Thou art at the highest level of spell ability!
#Thou cannot acquire new spells yet.
# spell level 
# will cost thee 
# in gold. 
#The spell Sages refuse to teach you until you can pay!
#Will you pay?
#The Spell Sages have taught you the lore.
#Which mage seeks to change his class?
#Thou must know at least 3 spell levels in your present art first.
#Conjurer
#Magician
#Sorcerer
#Wizard
#Thou cannot change to an old class!
#Done!
#The Guild leaders prepare to weigh thy merits.
#Who shall be reviewed?
#The head of the review board speaks, "Before we allow you to advance, you must demonstrate your knowledge of Skara Brae."
#"You had best study your maps more."
#"Well done!"
#The guild leaders deem that 
# still needth 
#prior to advancement...
# hath earned a level of advancement...

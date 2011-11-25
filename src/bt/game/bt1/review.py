import pygame
import bt.game.action as action
from bt.game.handler import ImageDisplayHandler, DefaultBuildingHandler

review = DefaultBuildingHandler("inside/review.png", """Wouldst thou like to be reviewed for:

Advancement
Spell Acquiring
Class Change
""")
#Review board
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

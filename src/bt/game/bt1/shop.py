import pygame
import bt.game.action as action
from bt.game.handler import ImageDisplayHandler, DefaultBuildingHandler

shop = DefaultBuildingHandler("inside/shop.png", "Welcome to Garth's Equipment Shoppe, oh wealthy travellers!", location="The Shoppe")
#The shoppe is closed at night.
#Which of you is interested in my fine wares?
#Greetings, 
#. Would you like to:
#Buy an item.
#Sell an item.
#Identify item.
#Pool gold.
#Done.
#You have:
# gold.
#The Shoppe
#You have no items.
#Which item:
#That item is known already.
#Done!>

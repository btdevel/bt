import pygame
import bt.game.action as action
from bt.game.handler import ImageDisplayHandler, DefaultBuildingHandler
harkyn = DefaultBuildingHandler("inside/castle.png", """This is the entry chamber to Harkyn's Castle. It is not guarded, but a sign threatens trespassers with death. You can:

Take stairs up

""", location="Castle"
)


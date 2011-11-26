import pygame
import bt.game.action as action
from bt.game.handler import ImageDisplayHandler

class CreditsHandler(ImageDisplayHandler):
    def __init__(self, filename, message, exit_action=action.exit_building(), location=""):
        ImageDisplayHandler.__init__(self, filename, location=location)
        self.add_key_event((pygame.K_ESCAPE, 0), exit_action)
        self.add_key_event("cC", exit_action)
        self.message = message

    def redraw(self, state):
        # this should go into some "enter" method
        ImageDisplayHandler.redraw(self, state)
        with state.message_view_ctx() as msg:
            msg.update_flag = True
            msg.clear()
            msg.message(self.message)
            msg.message("\n(CONTINUE)", center=True)
        print "building message printed"


credits = CreditsHandler("inside/credits.png", """\n\n\n\n\n\n\n\n\nTHE BARD'S TALE IBM was from an original design by Michael Cranford.
 
It was created at Interplay Productions, in Newport Beach, California.
 
Interplay wishes to express its gratitude to a number of people who worked on THE BARD'S TALE:
 
Todd Camasta
(Artwork)
 
Troy P. Worrell
(Programming)
 
Dave Warhol
Aarn Abbey
(Music)
 
Brian Fargo
(Dungeons)
 
Joe Ybarra
(Producer)
""", location="Bard's Tale")

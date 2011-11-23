import pygame
from bt.game.ui import EventHandler
import bt.game.action as action

class DefaultBuildingHandler(EventHandler):
    def __init__(self, filename, message, exit_action=action.exit_building()):
        EventHandler.__init__(self)
        self.add_key_event((pygame.K_ESCAPE, 0), exit_action)
        self.add_key_event("eE", exit_action)
        self.filename = filename
        self.message = message


    def redraw(self, state):
        state.ui.clear_view()
        state.ui.blitim(self.filename)
        state.ui.update_display()
        # this should go into some "enter" method
        state.ui.clear_message()
        state.ui.message(self.message)
        state.ui.message("     (EXIT)")

class EmptyBuildingHandler(DefaultBuildingHandler):
    def __init__(self, filename, message):
        DefaultBuildingHandler.__init__(self, filename, message)

    def key_event(self, state, key):
        if EventHandler.key_event(self, state, key):
            return True
        action.exit_building()(state)
        return True

empty = EmptyBuildingHandler("inside/empty.png", "You're in an empty building.")

stable = EmptyBuildingHandler("inside/empty.png", "Sorry, friends, all the horses have been eaten by creatures!")

temple = DefaultBuildingHandler("inside/temple.png", "Welcome, oh weary ones, to our humble temple. Who needeth healing?")
# is in bad shape, indeed. It will cost 
#The priests lay hands on him...
#...and he is healed!
# has been drained of life force. It will cost 
# has wounds which need tending. It will cost 
#any healing.
#1OO Blessings
#Great gods
#Greater gods
#Thief Temple
#Tmpl of Kiosk
#Greatest gods
#Mad God

madgod = DefaultBuildingHandler("inside/temple.png", "This is the temple of the Mad God. What is thy business, unbeliever?")
#TARJAN
#Speak to priest
#Only those who know the name of the Mad One are welcome.
#What wilt thou say?
#"Quit thy babbling," the priest says.
#"Speak not the name of the High One so loudly, lest he awaken," the priest says. "Enter the catacombs, believer."


shop = DefaultBuildingHandler("inside/shop.png", "Welcome to Garth's Equipment Shoppe, oh wealthy travellers!")
#The shoppe is closed at night.
#The Shoppe
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


pub = DefaultBuildingHandler("inside/pub.png", "Hail, travelers! Step to the bar and I'll draw you a tankard.")
#"The guardians can be deadly," the barkeep smirks.
#"A taste of wine might turn to ready adventure," the barkeep chuckles.
#"Look for the Review Board on Trumpet Street," the barkeep whispers.
#"The gates cannot be scaled, but an entrance always exists," the barkeep stutters.
#"The Stone Golem has been spoken of twofold," the barkeep smiles.
#"The Spectre Snare can draw in even the mightiest," the barkeep grumbles.
#You can:
#Order a drink
#Talk to barkeep
#Who will drink?
#Seat thyself, 
#. We've got...
#Beer
#Mead
#Foul spirits
#Ginger Ale
#Wine
#What'll it be?
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

roscoes = DefaultBuildingHandler("inside/roscoes.png", """Welcome, my friends, to Roscoe's Energy Emporium. 
Who needeth spell points restored?""")
#Roscoe's
#restoration.
# has some definite spell point problems. It will cost 
#Roscoe re-energizes him.

harkyn = DefaultBuildingHandler("inside/castle.png", """This is the entry chamber to Harkyn's Castle. 
It is not guarded, but a sign threatens trespassers with death. 
You can:

Take stairs up"""
)
#Castle

kylearan = DefaultBuildingHandler("inside/empty.png", """This is the entry chamber to Kylearan's Amber Tower. 
A stairwell leads up to a lofty level of chambers.
You can:

Take stairs""")
#Amber Tower

mangar = DefaultBuildingHandler("inside/empty.png", """This is the entry chamber to Mangar's Tower. 
A stairwell leads up to the first level of traps and terrors. 
You can:

Take stairs""")
#Magic mouth
#A magic mouth on the wall speaks to you: "Despised 
#ones, none save Mangar may enter his demesne."
#The Tower


credits = DefaultBuildingHandler("inside/credits.png", """\n\n\n\n\n\n\n\n\nTHE BARD'S TALE IBM was from an original design by Michael Cranford.

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
""")


class TurnBackHandler(DefaultBuildingHandler):
    def __init__(self, filename, message, display=""):
        DefaultBuildingHandler.__init__(self, filename, message, exit_action=action.turn_back())

class IronGateHandler(TurnBackHandler):
    def __init__(self, filename, message, display=""):
        DefaultBuildingHandler.__init__(self, filename, message, exit_action=action.turn_back())

class GuardianHandler(EventHandler):
    def __init__(self, filename, message, display=None):
        EventHandler.__init__(self)
        self.add_key_event("lL", action.turn_back())
        self.add_key_event("aA", action.compose(action.enter_city(), action.message("The statue gives up...")))
        self.filename = filename
        self.message = message

    def redraw(self, state):
        state.ui.clear_view()
        state.ui.blitim(self.filename)
        state.ui.update_display()
        # this should go into some "enter" method
        state.ui.clear_message()
        state.ui.message(self.message)


statue = GuardianHandler("city/statue.png", """You stand before a gate, which is guarded by the statue of a XYZ. You can:
Attack it.
Leave it.""", display="Guardian")


iron_gate_mangar = IronGateHandler("city/gate.png", "You stand before an iron gate, beyond which stands Mangar's tower.", display="Iron Gate")
iron_gate_kylearan = IronGateHandler("city/gate.png", "You stand before an iron gate, beyond which stands Kylearan's tower.", display="Iron Gate")

city_gate = TurnBackHandler("city/city_gate.png", "You stand before the city gates, which are blocked by a gigantic snow drift.", display="")


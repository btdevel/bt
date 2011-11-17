# this module contains just some ideas, nothing of which is finished yet

class CharacterClass(object):
    classes = []
    def __init__(self, id, name):
        self.id = id
        self.name = name

#warrior = CharClass( "Warrior", exp_needed, hp_per_level, magic, class_change, 
#                     modifiers, spell_table)

class CharacterRace(object):
    races = []
    def __init__(self, id, name):
        self.id = id
        self.name = name

#elf = CharRace( "Elf", modifiers )


class Character(object):
    def __init__(self):
        pass


class Party(object):
    def __init__(self):
        pass



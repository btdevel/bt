class CharClass(object):
    pass

warrior = CharClass( "Warrior", exp_needed, hp_per_level, magic, class_change, 
                     modifiers, spell_table)

class CharRace(object):
    pass

elf = CharRace( "Elf", modifiers )


class Character(object):
    pass

c = Character("EL CID", class=warrior, race=elf, str=10, dex=5)
c.gold
c.equipment
c.equipped

class Party(object):
    pass

party.add_char( c )

class GameState:
    pass

state.map
state.party
state.enemies (if in combat)

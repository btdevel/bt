# this module contains just some ideas, nothing of which is finished yet

class CharacterClass(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        Character.classes[id] = self
    def __str__(self):
        return self.name
#warrior = CharClass( "Warrior", exp_needed, hp_per_level, magic, class_change, 
#                     modifiers, spell_table)

class CharacterRace(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        Character.races[id] = self
    def __str__(self):
        return self.name

#elf = CharRace( "Elf", modifiers )


class Character(object):
    classes = {}
    races = {}

    def __init__(self, id=None):
        self.id = id
        self.name = ""
        self.status = 0
        self.race = 0
        self.char_class = 0
        self.curr_str = 0
        self.curr_int = 0
        self.curr_dex = 0
        self.curr_con = 0
        self.curr_lck = 0
        self.max_str = 0
        self.max_int = 0
        self.max_dex = 0
        self.max_con = 0
        self.max_lck = 0
        self.max_hp = 0
        self.curr_hp = 0
        self.max_sp = 0
        self.curr_sp = 0
        self.equip_buffer = []
        self.equipment = [0, ] * 8
        self.equipped = [False, ] * 8
        self.experience = 0
        self.gold = 0
        self.level = 0
        self.con_level = 0
        self.mag_level = 0
        self.sor_level = 0
        self.wiz_level = 0
        self.num_songs = 0

    def print_(self):
        print "Id: %d" % self.id
        print "Name:  %s" % self.name
        print "State: %s" % self.status
        print "Race:  %s (%d)" % (Character.races.get(self.race), self.race)
        print "Class: %s (%d)" % (Character.classes.get(self.char_class), self.char_class)
        print "St: %d/%d" % (self.curr_str, self.max_str)
        print "Iq: %d/%d" % (self.curr_int, self.max_int)
        print "Dx: %d/%d" % (self.curr_dex, self.max_dex)
        print "Cn: %d/%d" % (self.curr_con, self.max_con)
        print "Lk: %d/%d" % (self.curr_lck, self.max_lck)
        print "HP: %d/%d" % (self.curr_hp, self.max_hp)
        print "SP: %d/%d" % (self.curr_sp, self.max_sp)
        #self.equip_buffer = []
        #self.equipment = [0, ] * 8
        #self.equipped = [False, ] * 8
        print "Exp: %d" % self.experience
        print "Gold: %d" % self.gold
        print "Level: %d" % self.level
        print "SL Co: %d" % self.con_level
        print "SL Ma: %d" % self.mag_level
        print "SL So: %d" % self.sor_level
        print "SL Wi: %d" % self.wiz_level
        print "Bard songs: %d" % self.num_songs

    def __str__(self):
        return str(self.__dict__)

# Bitfield:
# Nuts=80h
# Poss=40h
# Para=20h
# Ston=10h
# Pois=08h
# Old=04h
# Dead=02h
# Alive=00h


class Party(object):
    def __init__(self):
        self.chars = []
        self.max_chars = 6
    def is_full(self):
        return len(self.chars)==self.max_chars
    def is_member(self, char):
        for c in self.chars:
            if c.name == char.name:
                return True
        return False
        
    def add(self, char):
        if self.is_member(char):
            return (False, "already_in_party")
        if self.is_full():
            return (False, "roster_full")
        self.chars.append(char)
        return (True,)



chardisp = ["inside/empty.png",
                             """N %(char_name)s
Race: %(char_race)s
Class: %(char_class)s
St: %(char_st)2d IQ: %(char_iq)2d  
Dx: %(char_dx)2d Cn: %(char_cn)2d
Lk: %(char_lk)2d HP: %(char_hp)2d
Lvl: %(char_level)2d HP: %(char_sppt)d
Exper: %(char_exp)d
Gold:  %(char_gold)d
    (POOL GOLD)
    (TRADE GOLD)
    (CONTINUE)"""]

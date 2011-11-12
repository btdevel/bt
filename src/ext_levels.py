import os

level=15

def generate_htree(bit_seq):
    "Generate a Huffman tree from a bit sequence."
    if bit_seq.next():
        val = 0
        bits = [1<<i for i in reversed(range(8))]
        for bit in bits:
            if bit_seq.next():
                val |= bit
        return val
    t0 = generate_htree(bit_seq)
    bit_seq.next()
    t1 = generate_htree(bit_seq)
    return [t0, t1]

def print_htree(t, prefix=""):
    "Print Huffman tree."
    if isinstance(t, int):
        print prefix + ": ", hex(t)
    else:
        print_htree(t[0], prefix+"0")
        print_htree(t[1], prefix+"1")

def decode(bit_seq, htree, num_decoded):
    "Decode bit sequence using a Huffman tree."
    def match(bit_seq, htree):
        if isinstance(htree, int):
            return htree
        bit = bit_seq.next()
        return match(bit_seq, htree[int(bit)])
                     
    for i in range(num_decoded):
        yield match(bit_seq, htree)

def make_bit_seq(byte_arr):
    "Return a byte array as generator, so that it can be read as a sequence of bits."
    bits = [1<<i for i in reversed(range(8))]
    for byte in byte_arr:
        for bit in bits:
            yield bool(byte&bit)

def read_long(byte_arr, offset):
    return  byte_arr[offset]<<24 |byte_arr[offset+1]<<16 | byte_arr[offset+2]<<8 | byte_arr[offset+3]

def decode_from_offset(inp, offset):
    decomp_size = read_long(inp, offset)
    comp_size = read_long(inp, offset+4)
    start = offset + 8
    bit_seq = make_bit_seq(inp[start:start+comp_size])
    htree = generate_htree(bit_seq)
    return list(decode(bit_seq, htree, decomp_size))

def load_file(name):
    global bt_dir
    filename=os.path.join(bt_dir, name)
    inp = bytearray(open(filename).read())
    return inp

def read_level(level):
    "Read a BT1 level (0=Wine Cellar,4=Catacombs1,7=Castle1,10=Kylearan,11=Mangar1,15=Mangar5) from disk and decode it."
    inp = load_file("levs")
    offset = read_long(inp, level*4)
    return decode_from_offset(inp, offset)

def read_city_path():
    "Read BT1 city path file and decode it."
    inp = load_file("city.pat")
    return decode_from_offset(inp, offset=0)

def read_city_name():
    "Read BT1 city path file and decode it."
    inp = load_file("city.nam")
    return decode_from_offset(inp, offset=0)

def print_city():
    trans = {0: " ", # Street
             1: "1", 2: "2", 3: "3", 4: "4", # Houses
             0x0B: "A", # Adventurer's Guild
             0x12: "P", # Pub/Inn
             0x1C: "G", # Garth's Shop
             0x21: "T", # Temple
             0x2B: "R", # Review Board
             0x60: "S", # Statue
             0x68: "+", # Gate to Tower
             0x71: "C", # Catacombs/Mad God Temple
             0x78: "<", # Stairs from Sewers
             0x81: "I", # Interplay Credits
             0x89: "E", # Roscoe's Energy Emporium
             0x91: "K", # Kylearan's Tower
             0x9B: "H", # Harkyn's Castle
             0xA1: "M", # Mangar's Tower
             0xA8: "|", # City Gates
             }
    for i, c  in enumerate(read_city_path()):
        print trans.get(c, "?"),
        if (i+1) % 30 == 0: print

def print_streets():
    trans = {
        0x00: "Alley",
        0x01: "Rakhir",
        0x02: "Blacksmith",
        0x03: "Main",
        0x04: "Trumpet",
        0x05: "Grey Knife",
        0x06: "Stonework",
        0x07: "Emerald",
        0x08: "Hawk Scabbard",
        0x09: "Bard Blazon",
        0x0A: "Tempest",
        0x0B: "Fargoer",
        0x0C: "Blue Highway (a)",
        0x0D: "Night Archer",
        0x0E: "Serpent(skin)",
        0x0F: "Corbomite",
        0x10: "Sinister",
        0x11: "Marksman",
        0x12: "Dilvish",
        0x13: "Death Archer",
        0xFF: "Gran(d) Plaz",
        }
    def shorten(name):
        part = name.split(" ")
        return part[0][:2] if len(part)<2 else part[0][0]+part[1][0]

    m = read_city_path()
    for i, c  in enumerate(read_city_name()):
        if m[i] in {0, 0xa8, 0x60, 0x68, 0x78}:
            #print "%02x" % c,
            print shorten(trans.get(c, "__")),
        else:
            print "XX",
        if (i+1) % 30 == 0: print


bt_dir = "../content/msdos/Bard1"

print
print_city()

print
print_streets()

print
lev = read_level(level)
start = 0
length = 22*22 


for i, c in enumerate(lev[start:start+length]):
    print "%02x" % c,
    if (i+1) % 22 == 0: print

# The first byte (65) in binary is 01100101. Broken down, this looks like:
# first 2 bits: 01 represent the west wall
# second 2 bits: 10 represent a door to the east
# third 2 bits: 01 represent a wall to the south
# last 2 bits: 01 represent a wall to the north 



lev = read_level(level)
start = 0
length = 22*22 
dmap=[]
for i in xrange(2*22+1):
    dmap.append(bytearray(" "*(3*22+1)))

for j in xrange(22):
    for i in xrange(22):
        c = lev[start+i+22*j]
        print hex(c),
        mx=3*i+1
        my=2*(21-j)+1
        t=(c>>6)&3
        if t>0:
            dmap[my-1][mx-1]='+'
            dmap[my  ][mx-1]=' |D?'[t]
            dmap[my+1][mx-1]='+'
        t=(c>>4)&3
        if t>0:
            dmap[my-1][mx+2]='+'
            dmap[my  ][mx+2]=' |D?'[t]
            dmap[my+1][mx+2]='+'
        t=(c>>2)&3
        if t>0:
            dmap[my+1][mx-1]='+'
            dmap[my+1][mx:mx+2]=' -D?'[t]*2
            dmap[my+1][mx+2]='+'
        t=(c)&3
        if t>0:
            dmap[my-1][mx-1]='+'
            dmap[my-1][mx:mx+2]=' -D?'[t]*2
            dmap[my-1][mx+2]='+'
            
print
for s in dmap:
    print s

print 
print lev[start+length:start+length+28]

print
start=start+length+28
for i, c in enumerate(lev[start:start+length]):
    print "%02x" % c,
    if (i+1) % 22 == 0: print

print
print lev[start+length:]

print
print len(lev)


l=lev[start+length:]
l=map(lambda l: l&0x7F, l)
print bytearray(l)

# Which represents the events for Harkyn's castle lvl 3.
# The cluster of '04' at the bottom is the + shaped room with all the teleports in them (each 04 is a teleport)
# The cluster of '04' at the top right, represent the spinners and the confrontation with the Mad God. The '04' a bit to the left represents the anit-magic zone when you enter the Mad Gods chamber.
# A bit below and to the left, there's another '04' which is the text before you enter the barracks (5, 11 on the map) (A sign on the wall reads, 'The Barracks.')
# The encounter with the berserkers doesn't show. Probably because I took the memory dump after I killed them and was still inside that level.



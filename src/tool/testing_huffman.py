import os, sys

from btfile import *

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")


# Part 1: Reading the file, big endian, little endian
byte_arr = load_file("bardtit", msdos_bt1_path)
byte_arrs = load_indexed_file("levs", msdos_bt1_path)

for i in xrange(20):
    print "%02X" % byte_arrs[0][i],
print


# Part 2: Iterating bit by bit, Reading the tree
bit_seq = make_bit_seq(byte_arr[8:])
htree = read_htree(bit_seq)
print htree


# Part 3: Iterating and printing the tree
print_htree(htree)


# Part 4: Decoding the data
data = decode_chunk(byte_arr, endians=(GUESS, GUESS))
for i in xrange(20):
    print "%02X" % data[i],
print

# Part 5: Building a new tree
count = count_data(data)
print_htree(htree, count)
print

htree = build_htree(data)
print_htree(htree, count)
print
    
# Part 6: Encoding the data with the tree

byte_arr=bytearray()
byte_arr.append(1)
byte_arr.append(15)
bit_writer=BitWriter(byte_arr)
for i in xrange(6):
    bit_writer.write_bit(True)
    bit_writer.write_bit(False)
print bit_writer.flush()
write_long(byte_arr, 0x123456, 10, BIG_ENDIAN)
write_long(byte_arr, 0x123456, 16, LITTLE_ENDIAN)
for i in byte_arr:
    print "%02X" % i,
print
print read_long( byte_arr, 10, GUESS)
print read_long( byte_arr, 10, BIG_ENDIAN)
print read_long( byte_arr, 16, GUESS)
print read_long( byte_arr, 16, LITTLE_ENDIAN)

table=bytearray(range(256))
table[0x00]=0xFF
data=data.translate(table)
count=count_data(data)
byte_arr = encode_chunk(data, htree=None)
for i in byte_arr:
    print "%02X" % i,
bit_seq = make_bit_seq(byte_arr[8:])
htree2 = read_htree(bit_seq)
print_htree(htree2, count)

#
test_txt = """Long ago, when magic still prevailed, the evil wizard Mangar the Dark
threatened a small but harmonious country town called Skara Brae. Evil
creatures oozed into Skara Brae and joined his shadow domain. Mangar froze
the surrounding lands with a spell of Eternal Winter, totally isolating
Skara Brae from any possible help. Then, one night the town militiamen
all disappeared

The future of Skara Brae hung in the balance. And who was left to resist?
Only a handful of unproven young Warriors, junior Magic Users, a couple of
Bards barely old enough to drink, and some out of work Rogues.

You are there. You are the leader of this ragtag group of freedom fighters.
Luckily you have a Bard with you to sing your glories, if you survive. For
this is the stuff of legends. And so the story begins...
"""
data = bytearray(test_txt)
print test_txt
byte_arr = encode_chunk(data)
print len(test_txt), len(byte_arr)
for i in byte_arr[:20]:
    print "%02X" % i,
print
rec = decode_chunk(byte_arr)
print rec


# Part 7: Writing the files (normal and indexed)

test=[0]*3
test[0] = """Long ago, when magic still prevailed, the evil wizard Mangar the Dark
threatened a small but harmonious country town called Skara Brae. Evil
creatures oozed into Skara Brae and joined his shadow domain. Mangar froze
the surrounding lands with a spell of Eternal Winter, totally isolating
Skara Brae from any possible help. Then, one night the town militiamen
all disappeared"""
test[1]="""The future of Skara Brae hung in the balance. And who was left to resist?
Only a handful of unproven young Warriors, junior Magic Users, a couple of
Bards barely old enough to drink, and some out of work Rogues."""

test[2]="""You are there. You are the leader of this ragtag group of freedom fighters.
Luckily you have a Bard with you to sing your glories, if you survive. For
this is the stuff of legends. And so the story begins...
"""



data = []
for txt in test:
    data.append( encode_chunk(bytearray(txt)) )
write_indexed_file("foo", data)
newdata=load_indexed_file("foo")
print "Num chunks:", len(newdata)
for t in newdata:
    print "chunk len:", len(t)
    print decode_chunk(t)





# Part 8: Examples
#  a) Inverting the BardScreen
#  b) Removing all walls from the Catacombs


# Part 9: Creating some utility programs 


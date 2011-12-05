import os, sys

from bt.extract.btfile import *

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")

inp = load_file("bardtit", msdos_bt1_path)


offset=0
endians=(GUESS, GUESS)
decomp_size = read_long(inp, offset, endian=endians[0])
comp_size = read_long(inp, offset + 4, endian=endians[1])
start = offset + 8
bit_seq = make_bit_seq(inp[start:start + comp_size], comp_size)
htree = generate_htree(bit_seq)
data = decode(bit_seq, htree, decomp_size)



def count_data(data):
    count = [0] * 256
    for b in data:
        count[b]+=1
    return count

def build_htree(data, count=None):
    if not count:
        count = count_data(data)
    ht = sorted((count[i], i) for i in xrange(256))
    while len(ht)>1:
        sub_cnt=ht[0][0]+ht[1][0]
        sub_ht=[ht[0][1], ht[1][1]]
        ht[0:2]=[(sub_cnt, sub_ht)]
        ht=sorted(ht)
    return ht[0][1]

count = count_data(data)
print count
print_htree(htree, count=count)

if True:
    htree = build_htree(data)
    print
    print
    #print htree

    print_htree(htree, count=count)


"""
Reading the file, big endian, little endian
Iterating bit by bit
Reading the tree
Iterating and printing the tree
Decoding the data
Building a new tree (not necessary)
Encoding the data with the tree
Writing the file
Reading and writing indexed files
An example: Removing all traps/darkness and other mean stuff from KylTower

Explain a little bit of Python along the way
"""

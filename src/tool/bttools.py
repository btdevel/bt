import os, sys

from btfile import *

def expand(infile, outfile):
    byte_arr = load_file(infile)
    data = decode_chunk(byte_arr)
    write_file(outfile, data)

def compress(infile, outfile):
    data = load_file(infile)
    byte_arr = encode_chunk(data)
    write_file(outfile, byte_arr)

def expand_indexed(infile, outfile_pattern):
    byte_arrs = load_indexed_file(infile)
    for i in xrange(len(byte_arrs)):
        data = decode_chunk(byte_arrs[i])
        write_file(outfile_pattern%i, data)

def compress_indexed(infile_pattern, outfile):
    from glob import glob
    byte_arrs = []
    for filename in sorted(glob(infile_pattern)):
        data = load_file(filename)
        byte_arrs.append(encode_chunk(data))
    write_indexed_file(outfile, byte_arrs)


if True:
    expand( "b0.huf", "b0.bin" )
    compress( "b0.bin", "b02.huf" )
    expand_indexed( "levs",  "levs-%02d.bin" )
    compress_indexed( "levs-*.bin", "levr" )
    expand_indexed( "levr",  "levr-%02d.bin" )


def bit_length_compressed(data, htree):
    count=count_data(data)
    bl = 0
    for (val, bits) in iterate_htree(htree):
        bl += count[val] * len(bits)
    return bl

byte_arr = load_file("b0.huf")
#byte_arr = load_file("b02.huf")
bit_seq = make_bit_seq(byte_arr[8:])
htree = read_htree(bit_seq)
data = decode_chunk(byte_arr)
count=count_data(data)
print_htree(htree, count)
bl=bit_length_compressed(data, htree)
print "bl1: %d = 0x%04x" % (bl, bl)

htree = build_htree(data)
bl=bit_length_compressed(data, htree)
print "bl2: %d = 0x%04x" % (bl, bl)



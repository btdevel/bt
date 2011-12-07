# Part 1: Reading in the files
import os

LITTLE_ENDIAN = 0
BIG_ENDIAN = 1
GUESS = 2

def load_file(name, path=".", hex=False):
    """Load a file and return as raw bytearray"""
    filename = os.path.join(path, name)
    filename = filename.replace('/', os.path.sep)
    with open(filename, "rb") as f:
        byte_arr = bytearray(f.read())
    if hex:
        byte_arr = hex_to_bin(byte_arr)
    return byte_arr

def read_long(byte_arr, offset, endian=GUESS):
    """Read a long value from a byte array using a given endian or
    guessing the endian"""
    if endian == GUESS:
        return min(read_long(byte_arr, offset, BIG_ENDIAN),
                   read_long(byte_arr, offset, LITTLE_ENDIAN))
    b = byte_arr[offset:offset + 4]
    if endian == LITTLE_ENDIAN:
        b.reverse()
    return  b[0] << 24 | b[1] << 16 | b[2] << 8 | b[3]

def load_indexed_file(name, path=".", endian=GUESS):
    """Read in an indexed files and return an array of bytearrays."""
    byte_arr = load_file(name, path)
    num_chunks = read_long(byte_arr, 0, endian) // 4

    def get_chunk(byte_arr, index, num_chunks):
        start = read_long(byte_arr, index * 4, endian)
        if index < num_chunks - 1:
            end = read_long(byte_arr, index * 4 + 4, endian)
        else:
            end = len(byte_arr)
        return byte_arr[start:end]

    byte_arrs = []
    for index in xrange(num_chunks):
        byte_arrs.append(get_chunk(byte_arr, index, num_chunks))
    return byte_arrs

# Part 2: Reading in the tree
def make_bit_seq(byte_arr, max_bits= -1):
    """Return a byte array as generator, so that it can be read as a
    sequence of bits."""
    bits = [1 << i for i in reversed(range(8))]
    for byte in byte_arr:
        for bit in bits:
            yield bool(byte & bit)
            max_bits -= 1
            if max_bits == 0 :
                raise Exception("Too many bits read from bit seq")

def read_htree(bit_seq):
    """Generate a Huffman tree from a bit sequence."""
    if bit_seq.next():
        val = 0
        bits = [1 << i for i in reversed(range(8))]
        for bit in bits:
            if bit_seq.next():
                val |= bit
        return val
    t0 = read_htree(bit_seq)
    bit_seq.next()
    t1 = read_htree(bit_seq)
    return [t0, t1]

# Part 3: Iterating and printing the tree
def iterate_htree(htree):
    """Iterate over a Huffman tree yielding all pairs of values and
    bit sequences."""
    def htreeiter(t, prefix):
        if isinstance(t, int):
            yield t, prefix
        else:
            for x in htreeiter(t[0], prefix + "0"):
                yield x
            for x in htreeiter(t[1], prefix + "1"):
                yield x
    return htreeiter(htree, "")

def print_htree(htree, count=None):
    """Print Huffman tree (optionally showing counts related to the
    data)."""
    for (val, bits) in iterate_htree(htree):
        if count:
            print  "%02d %s: %02x (%d)" % (len(bits), bits, val, count[val])
        else:
            print  "%s: %02x" % (bits, val)

# Part 4: Decoding the data using the Huffman trees
def decode(bit_seq, htree, decomp_size):
    """Decode bit sequence using a given Huffman tree."""
    def match(bit_seq, htree):
        if isinstance(htree, int):
            return htree
        bit = bit_seq.next()
        return match(bit_seq, htree[int(bit)])

    byte_arr = bytearray(decomp_size)
    for i in xrange(decomp_size):
        byte_arr[i] = match(bit_seq, htree)
    return byte_arr

def decode_chunk(byte_arr, endians=(GUESS, GUESS)):
    """Decode a chunk of Huffman encoded data"""
    decomp_size = read_long(byte_arr, 0, endian=endians[0])
    comp_size = read_long(byte_arr, 4, endian=endians[1])
    start = 8
    bit_seq = make_bit_seq(byte_arr[start:], comp_size)
    htree = read_htree(bit_seq)
    data = decode(bit_seq, htree, decomp_size)
    # there should be a check here that no bit is left over in the sequence
    return data

# Part 5: Build a new Huffman tree.
def count_data(data):
    count = [0] * 256
    for b in data:
        count[b] += 1
    return count

def build_htree(data, count=None):
    if not count:
        count = count_data(data)
    ht = sorted((count[i], i) for i in xrange(256) if count[i] > 0)
    while len(ht) > 1:
        sub_cnt = ht[0][0] + ht[1][0]
        sub_ht = [ht[0][1], ht[1][1]]
        ht[0:2] = [(sub_cnt, sub_ht)]
        ht = sorted(ht)
    return ht[0][1]


# Part 6: Encoding the data and writing into a buffer
def write_long(byte_arr, value, offset=0, endian=BIG_ENDIAN):
    """Write a long value into a byte array using a given endian"""
    while len(byte_arr) < offset + 4:
        byte_arr.append(0)
    if endian == BIG_ENDIAN:
        offset += 3
        dir = -1
    else:
        dir = 1
    for i in xrange(4):
        byte_arr[offset] = value & 0xFF
        value >>= 8
        offset += dir

class BitWriter(object):
    def __init__(self, byte_arr):
        self.byte_arr = byte_arr
        self.total = 0
        self.bits = 0
        self.byte = 0
    def write_bit(self, bit):
        self.total += 1
        self.bits += 1
        self.byte = self.byte << 1 | (1 if bit else 0)
        if self.bits == 8:
            self.flush()
    def flush(self):
        if self.bits:
            self.byte_arr.append(self.byte << (8 - self.bits))
        self.byte = 0
        self.bits = 0
        return self.total

def write_htree(bit_writer, htree):
    """Write a Huffman tree into a bit writer."""
    if isinstance(htree, int):
        bit_writer.write_bit(True)
        val = htree
        bits = [1 << i for i in reversed(range(8))]
        for bit in bits:
            bit_writer.write_bit(bool(val & bit))
    else:
        bit_writer.write_bit(False)
        write_htree(bit_writer, htree[0])
        bit_writer.write_bit(False)
        write_htree(bit_writer, htree[1])

def encode_data(bit_writer, htree, data):
    """Decode bit sequence using a given Huffman tree."""
    htable = [""] * 256;
    for (val, bits) in iterate_htree(htree):
        htable[val] = bits

    for b in data:
        for c in htable[b]:
            bit_writer.write_bit(c == "1")

def encode_chunk(data, htree=None, endians=(BIG_ENDIAN, BIG_ENDIAN)):
    """Decode a chunk of Huffman encoded data"""
    byte_arr = bytearray()
    decomp_size = len(data)
    comp_size = 0
    write_long(byte_arr, decomp_size, 0)
    write_long(byte_arr, comp_size, 4)

    if htree == None:
        htree = build_htree(data)
    bit_writer = BitWriter(byte_arr)
    write_htree(bit_writer, htree)
    encode_data(bit_writer, htree, data)
    comp_size = bit_writer.flush()
    write_long(byte_arr, comp_size, 4)
    return byte_arr

# Part 7: Writing the files
def write_file(name, byte_arr, path=".", hex=False):
    """Write data to a file."""
    filename = os.path.join(path, name)
    filename = filename.replace('/', os.path.sep)
    if hex:
        byte_arr = bin_to_hex(byte_arr)
    with open(filename, "wb") as f:
        f.write(byte_arr)

def write_indexed_file(name, byte_arrs, path=".", endian=BIG_ENDIAN):
    index = bytearray()
    offset = len(byte_arrs) * 4
    indexpos = 0
    for byte_arr in byte_arrs:
        write_long(index, offset, indexpos)
        offset += len(byte_arr)
        indexpos += 4
    byte_arrs.insert(0, index)

    byte_arr = bytearray().join(byte_arrs)
    write_file(name, byte_arr, path)

# Part 9: Some tools
def expand(infile, outfile, hex=False):
    byte_arr = load_file(infile)
    data = decode_chunk(byte_arr)
    write_file(outfile, data, hex=hex)

def compress(infile, outfile, hex=False):
    data = load_file(infile, hex=hex)
    byte_arr = encode_chunk(data)
    write_file(outfile, byte_arr)

def expand_indexed(infile, outfile_pattern, hex=False):
    byte_arrs = load_indexed_file(infile)
    for i in xrange(len(byte_arrs)):
        data = decode_chunk(byte_arrs[i])
        write_file(outfile_pattern % i, data, hex=hex)

def compress_indexed(infile_pattern, outfile, hex=False):
    from glob import glob
    byte_arrs = []
    for filename in sorted(glob(infile_pattern)):
        data = load_file(filename, hex=hex)
        byte_arrs.append(encode_chunk(data))
    write_indexed_file(outfile, byte_arrs)

#
def bin_to_hex(byte_arr):
    out = bytearray()
    for i, b in enumerate(byte_arr):
        out.extend("%02X " % b)
        if i % 16 == 0xF:
            out.extend("\n")
    return out


def hex_to_bin(byte_arr):
    byte_arr = byte_arr.translate(bytearray(range(256)), " \n\r\t")
    out = bytearray().fromhex(str(byte_arr))
    return out

#

def get_identity_htree():
    return build_htree(data=bytearray(xrange(256)))

def identity_recompress(filename):
    id_htree = get_identity_htree()
    byte_arr = load_file(filename)
    data = decode_chunk(byte_arr)
    byte_arr = encode_chunk(data, htree=id_htree)
    write_file(filename, byte_arr)

def identity_recompress_indexed(filename):
    id_htree = get_identity_htree()
    byte_arrs = load_indexed_file(filename)
    for i in xrange(len(byte_arrs)):
        data = decode_chunk(byte_arrs[i])
        byte_arrs[i] = encode_chunk(data, htree=id_htree)
    write_indexed_file(filename, byte_arrs)



# Some other stuff 

def bit_length_compressed(data, htree):
    count = count_data(data)
    bl = 0
    for (val, bits) in iterate_htree(htree):
        bl += count[val] * len(bits)
    return bl




import os

LITTLE_ENDIAN = 0
BIG_ENDIAN = 1
GUESS = 2

def generate_htree(bit_seq):
    "Generate a Huffman tree from a bit sequence."
    if bit_seq.next():
        val = 0
        bits = [1 << i for i in reversed(range(8))]
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
        print_htree(t[0], prefix + "0")
        print_htree(t[1], prefix + "1")

def decode(bit_seq, htree, num_decoded):
    "Decode bit sequence using a Huffman tree."
    def match(bit_seq, htree):
        if isinstance(htree, int):
            return htree
        bit = bit_seq.next()
        return match(bit_seq, htree[int(bit)])

    byte_arr = bytearray(num_decoded)
    for i in xrange(num_decoded):
        byte_arr[i] = match(bit_seq, htree)
    return byte_arr

def make_bit_seq(byte_arr, max_bits= -1):
    "Return a byte array as generator, so that it can be read as a sequence of bits."
    bits = [1 << i for i in reversed(range(8))]
    for byte in byte_arr:
        for bit in bits:
            yield bool(byte & bit)
            max_bits -= 1
            if max_bits == 0 :
                raise Exception("Too many bits read from bit seq")

def read_long(byte_arr, offset, endian=GUESS):
    if endian == GUESS:
        return min(read_long(byte_arr, offset, endian=BIG_ENDIAN),
                    read_long(byte_arr, offset, endian=LITTLE_ENDIAN))
    b = byte_arr[offset:offset + 4]
    if endian == LITTLE_ENDIAN:
        b.reverse()
    return  b[0] << 24 | b[1] << 16 | b[2] << 8 | b[3]

def decode_from_offset(inp, offset, endians=(GUESS, GUESS)):
    decomp_size = read_long(inp, offset, endian=endians[0])
    comp_size = read_long(inp, offset + 4, endian=endians[1])
    start = offset + 8
    bit_seq = make_bit_seq(inp[start:start + comp_size], comp_size)
    htree = generate_htree(bit_seq)
    data = decode(bit_seq, htree, decomp_size)

    try:
        bit_seq.next()
    except:
        # this should happen
        return data
    #print "WARNING: Not enough bits read from bit seq"
    return data

def load_file(name, path="."):
    filename = os.path.join(path, name)
    inp = bytearray(open(filename).read())
    return inp

def load_compressed_file(name, path=".", endians=(GUESS, GUESS)):
    inp = load_file(name, path)
    return decode_from_offset(inp, offset=0, endians=endians)

def load_indexed_file(name, path=".", index= -1, endians=(GUESS, GUESS, GUESS)):
    inp = load_file(name, path)
    num = read_long(inp, offset=0, endian=endians[0]) / 4
    if index == -1:
        data = []
        for i in xrange(num):
            offset = read_long(inp, i * 4, endian=endians[0])
            data.append(decode_from_offset(inp, offset, endians=endians[1:3]))
    else:
        offset = read_long(inp, index * 4)
        data = decode_from_offset(inp, offset, bigendians=endians[1:3])
    return data

def show_compressed_file_info(name, path=".", endians=(GUESS, GUESS)):
    filename = os.path.join(path, name)
    inp = load_file(name, path)
    decomp_size = read_long(inp, 0, endian=endians[0])
    comp_size = read_long(inp, 4, endian=endians[1])
    print "%s: compressed %d bytes (%d bits), decompressed %d bytes" \
        % (filename, (comp_size + 7) // 8, comp_size, decomp_size)

def show_indexed_file_info(name, path=".", endians=(GUESS, GUESS, GUESS)):
    filename = os.path.join(path, name)
    inp = load_file(name, path)
    num = read_long(inp, offset=0, endian=endians[0]) / 4
    print "%s: %d chunks of data" % (filename, num)
    for i in xrange(num):
        offset = read_long(inp, i * 4, endian=endians[0])
        decomp_size = read_long(inp, offset, endian=endians[1])
        comp_size = read_long(inp, offset + 4, endian=endians[2])
        print " chunk %d: compressed %d bytes (%d bits), decompressed %d bytes" \
            % (i, (comp_size + 7) // 8, comp_size, decomp_size)






def rle_decode(byte_arr):
    ROWS = 128
    COLS = 160
    screen = []
    for i in xrange(ROWS):
        screen.append([0, ] * COLS)

    def make_seq(byte_array):
        for b in byte_array:
            yield b

    seq = make_seq(byte_arr)
    row = 0
    col = 0
    val = 0
    run = 0

    tag_next_run = seq.next()
    tag_next_pos = seq.next()
    while True:
        if run == 0:
            chr = seq.next()
            if chr == tag_next_run:
                run = seq.next() + 3
                val = seq.next()
                continue
            elif chr == tag_next_pos:
                row = seq.next()
                col = seq.next()
                if col == 0xff:
                    return screen
                continue
            else:
                val = chr
        else:
            run -= 1

        screen[row][col // 4] = val
        row += 2;
        if row >= ROWS:
            row -= ROWS
            col += 4
            if col >= COLS:
                row += 1
                if row >= 2:
                    return screen
                col = 0
    return screen

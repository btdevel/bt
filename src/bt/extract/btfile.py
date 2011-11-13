import os

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

    for i in range(num_decoded):
        yield match(bit_seq, htree)

def make_bit_seq(byte_arr):
    "Return a byte array as generator, so that it can be read as a sequence of bits."
    bits = [1 << i for i in reversed(range(8))]
    for byte in byte_arr:
        for bit in bits:
            yield bool(byte & bit)

def read_long(byte_arr, offset):
    return  byte_arr[offset] << 24 | byte_arr[offset + 1] << 16 | byte_arr[offset + 2] << 8 | byte_arr[offset + 3]

def decode_from_offset(inp, offset):
    decomp_size = read_long(inp, offset)
    comp_size = read_long(inp, offset + 4)
    start = offset + 8
    bit_seq = make_bit_seq(inp[start:start + comp_size])
    htree = generate_htree(bit_seq)
    return list(decode(bit_seq, htree, decomp_size))

def load_file(name, path="."):
    filename = os.path.join(path, name)
    inp = bytearray(open(filename).read())
    return inp

def load_compressed_file(name, path="."):
    inp = load_file(name, path)
    return decode_from_offset(inp, offset=0)

def load_indexed_file(name, path=".", index= -1):
    inp = load_file(name, path)
    num = read_long(inp, offset=0) / 4
    if index == -1:
        data = []
        for i in xrange(num):
            offset = read_long(inp, i * 4)
            data.append(decode_from_offset(inp, offset))
    else:
        offset = read_long(inp, index * 4)
        data = decode_from_offset(inp, offset)
    return data

def show_compressed_file_info(name, path="."):
    filename = os.path.join(path, name)
    inp = load_file(name, path)
    decomp_size = read_long(inp, 0)
    comp_size = read_long(inp, 4)
    print "%s: compressed %d bytes (%d bits), decompressed %d bytes" \
        % (filename, (comp_size + 7) // 8, comp_size, decomp_size)

def show_indexed_file_info(name, path="."):
    filename = os.path.join(path, name)
    inp = load_file(name, path)
    num = read_long(inp, offset=0) / 4
    print "%s: %d chunks of data" % (filename, num)
    for i in xrange(num):
        offset = read_long(inp, i * 4)
        decomp_size = read_long(inp, offset)
        comp_size = read_long(inp, offset + 4)
        print " chunk %d: compressed %d bytes (%d bits), decompressed %d bytes" \
            % (i, (comp_size + 7) // 8, comp_size, decomp_size)

==============
 File Formats
==============


General
=======

Endianness
----------

Long integers in BT are sometimes saved in big and sometimes in little
endian format (see [http://en.wikipedia.org/wiki/Endianness]_). In big
endian format the most significant byte comes first, e.g. ``01 02 5E
AE`` means ``0x01<<24 + 0x02<<16 + 0x5E<<8 + 0xAE`` in big endian and
``0x01 + 0x02<<8 + 0x5E<<16 + 0xAE<<24`` in little endian. Big endian
is what humans are wont to read and what is used on PCs. In BT usage
is a bit arbitrary, e.g. in the MSDOS version the file ``dpics0``
starts with ``00 00 56 58 57 5a 01 00``, i.e. the first long is big
endian and the second one little endian, while ``dpics1`` starts with
``00 00 56 58 00 01 6a a2``, where both longs are big endian.

In BT often the following strategy works: decode the long value as big
endian and as little endian and take the smaller of both. Only in
cases where you expect the values to be really large, specify
endianness explicitly. Code example::

    def read_long_big(byte_arr, offset):
    	return  b[0] << 24 | b[1] << 16 | b[2] << 8 | b[3]

    def read_long_little(byte_arr, offset):
    	return  b[0] | b[1] << 8 | b[2] << 16 | b[3] << 14

    def read_long(byte_arr, offset, endian=GUESS):
        return min(read_long_big(byte_arr, offset),
                   read_long_little(byte_arr, offset)


Compressed Files (Huffman encoding)
-----------------------------------

Compression in BT is mostly done with Huffman encoding
[http://en.wikipedia.org/wiki/Huffman_coding]_. Any chunk of data
that is Huffman encoded, has the following structure:

* a long (4 bytes, mostly big endian) describing the number of bytes
of decompressed data
* a long (4 bytes, big or little endian) describing the number of
```bits``` of compressed data including the Huffman tree 
* the Huffman tree 
* the compressed data

The Huffman tree and the compressed data must be read bit by bit
always started with the highest bit of each byte. Both are directly
adjacent.

.. note:: Description of Huffman encoding goes here

Indexed Files
-------------

Description of indexed files goes here


Formats
=======

Levels
------

In BT1:

* Stored in 'levs' file, as indexed/compressed file, contains 15
  chunks of data, with:

  *  0 = Wine Cellar
  *  1 = Sewers 1
  *  2 = Sewers 2
  *  3 = Sewers 3
  *  4 = Catacombs 1
  *  5 = Catacombs 2
  *  6 = Catacombs 3
  *  7 = Harkyn's Castle 1
  *  8 = Harkyn's Castle 2
  *  9 = Harkyn's Castle 3
  * 10 = Kylearan's Tower
  * 11 = Mangar's Tower 1
  * 12 = Mangar's Tower 2
  * 13 = Mangar's Tower 3
  * 14 = Mangar's Tower 4
  * 15 = Mangar's Tower 5

* First 22*22 byte: wall data.  Ordering of bytes: west to east
  (fast), south to north (slow), zeroth byte (0N, 0E), first byte (0N,
  1E), 22nd byte (1N, 0E),

* Each byte contains 4 pairs of bits in the ordering: W, E, S,
  N. Meaning:

  * 00 -> Nothing
  * 01 -> Wall
  * 10 -> Door
  * 11 -> Secret Door 

* Flags (following 484 bytes):

  * bit 0 is set if there are stairs up.
  * bit 1 is set if there are stairs down.
  * bit 2 is set if there is a special (this includes spinners, magic
    squares, messages, magic mouths, etc. Everything that's not
    covered by one of the other bits.)
  * bit 3 is set if there's darkness
  * bit 4 is set if there's a trap.
  * bit 5 is set if there's a portal down
  * bit 6 is set if there's a portal up
  * bit 7 is set if there's a random encounter scheduled for this tile. 

* Thread: http://brotherhood.de/Bardstale/talefiles/board/viewtopic.php?t=788



City
----

Graphics
--------







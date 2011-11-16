==============
 File Formats
==============


General
=======

Compressed Files (Huffman encoding)
-----------------------------------

Description of Huffman encoding goes here

Indexed Files
-------------

Description of indexed files goes here

Endianness
----------

Description of big/little endian stuff goes here

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



MSDOS
=====

* `dpics0`, `dpics1`, `dpics2` contains 


Amiga
=====

Description of Amiga files goes here


Tools
=====

For Amiga
* UAE
* unadf
* uae_readdisk
* http://www.amigaemulator.org/useful
* adflib
* adfopus (win only I guess)



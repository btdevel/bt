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

* stored in 'levs' file, as indexed/compressed file

* First 22*22 byte: wall data. Each byte:
  * 00 -> Nothing
  * 01 -> Wall
  * 10 -> Door
  * 11 -> Secret Door 
  Ordering of two bit pairs: W, E, S, N
  Ordering of bytes: west to east (fast), south to north (slow), zeroth
  byte (0N, 0E), first byte (0N, 1E), 22nd byte (1N, 0E), 
  (Credits Horpner)

* Flags (following 484 bytes)
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


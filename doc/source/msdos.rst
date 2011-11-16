=======
 MSDOS
=======

File list
=========

The MSDOS version contains the following files:

47
  Probably the guild images

b0.huf
  Image for House type 0, compressed, using CGA palette

b1.huf
  Image for House type 1, compressed, using CGA palette

b2.huf
  Image for House type 2, compressed, using CGA palette

b3.huf
  Image for House type 3, compressed, using CGA palette

bard.exe
  The executable, can be used to locate game strings, other game data
  is difficult to obtain as the exe file is compressed (Does anybody
  know the decompression alg? Otherwise memdumps can be used to access
  that data; use the debug version of dosbox and the do a memdumpbin)

bardscr
  The main game screen, compressed, using CGA palette, the image is
  color separated: first come all blue pixel values, then all green
  pixel values, then red, and then the one for highlight. 

bardtit
  The title screen. Format is the same as bardscr.

bigpic
  Indexed/compressed file containing all the monsters, images inside 
  buildings, probably also city pictures except the big images of the 
  four house types.

cga_scr
  Not checked yet

city.nam
  Contains an index to the street names. Compressed.

city.pat
  Contains an index to the house numbers and specials in Skara Brae.

citypics.bin
  Not checked yet.

color.cmp
  No clue. 

color.rgb
  No clue.

comp
  No clue.

comp_tit
  No clue.

dpics0
  Contains the dungeon pictures for the standard dungeons. Image data
  is partitioned with partitioning like: 

    [(56, 88), (192, 86), (120, 54), (80, 33), (48, 17), (16, 40),
         (32, 88), (48, 85), (32, 52), (16, 31), (16, 15), (48, 32),
         (40, 18), (80, 8)]

dpics1
  Dungeon pictures for the dungeon levels in Mangar's tower. Otherwise 
  like dpics0 (endianess is a bit different for the first two longs
  here, than in dpics0 and dpics2
  
dpics2
  Dungeon pictures for the dungeon levels in the Catacombs. Otherwise 
  like dpics0.

graphics.drv
  Probably uninteresting

icons.bin
  Not checked.

items
  Contains the items available in Garth's equipment store. The value
  of byte x corresponds to the number of items Garth has to sell of
  item type x. A value of ``0xFF`` means an infinte supply.

levs
  Contains the levels. File is indexed and compressed. Longer
  description needs to be given elsewhere.

rgb
  Not checked.

rgb_tit
  Not checked.

tdy
  Not checked.

tdy_scr
  Not checked.

tdy_tit
  Not checked.

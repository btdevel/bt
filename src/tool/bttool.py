#!/usr/bin/env python
import os
import sys

import btfile

btpath = os.environ.get("BTPATH",".")

opt_args = [ "expand", "compress", "identity", "hex"]
val_args = [ "fileid"]

suppfiles = [
             ("level", "levs", True),
             ("pics", "bigpic", True),
             ("guild?", "47", True),
             ("citymap", "city.pat", False),
             ("streets", "city.nam", False),
             ("house1", "b0.huf", False),
             ("house2", "b1.huf", False),
             ("house3", "b2.huf", False),
             ("house4", "b3.huf", False),
             ("dungtype1", "dpics0", False),
             ("dungtype2", "dpics1", False),
             ("dungtype3", "dpics2", False),
             ("intro", "bardtit", False),
             ("gamescr", "bardpic", False),
             ]

def help_args(err=0, arg=""):
    print "USAGE: bttool {-expand|-compress|-identity} [-hex] -fileid=<file>"
    print " Specify one of:"
    print "  -expand: uncompress BT file to binary or hex format "
    print "  -compress: compress binary or hex file to BT file"
    print "  -identity: recompress BT file to use identity huffman tree"
    print
    print "  -fileid: file to work on (use filename or identifier)"
    print "         see below for a list of supported files"
    print "  -hex: expand as hex file (easier for humans to edit, worse for programs)"
    print
    print "  Supported Fileids:"
    for ident, filename, indexed in suppfiles:
        if indexed:
            print "     %s = %s (indexed)" % (ident, filename)
        else:
            print "     %s = %s" % (ident, filename)


    if err == 1:
        print "ERR: Exactly one of [" + " ".join(opt_args[:3]) + "] must be specified"
    elif err == 2:
        print "ERR: identity and hex together makes no sense"
    elif err == 3:
        print "ERR:unrecognised argument %s" % arg
    elif err == 4:
        print "ERR:unrecognised fileid: '%s'" % arg
    sys.exit(err)


if len(sys.argv) <= 1:
    help_args()

hex = False
expand = False
identity = False
compress = False
fileid = None
for arg in sys.argv[1:]:
    import __main__ as main_mod
    arg = arg.lstrip("-")
    args = map(str.strip, arg.split("="))
    if arg in opt_args:
        main_mod.__dict__[arg] = True
    elif args[0] in val_args:
        main_mod.__dict__[args[0]] = args[1]
    else:
        help_args(3, arg)

found = False
for (name, basename, indexed) in suppfiles:
    if fileid in [name, basename]:
        found = True
        break
if not found:
    help_args(4, fileid)

if hex:
    extension = "hex"
else:
    extension = "bin"

if expand:
    if compress or identity:
        help_args(1)
    infilename = os.path.join(btpath, basename)
    if indexed:
        outfilepat = "%s-%%02d.%s" % (basename, extension)
        btfile.expand_indexed(infilename, outfilepat, hex=hex)
    else:
        outfilename = "%s.%s" % (basename, extension)
        btfile.expand(infilename, outfilename, hex=hex)
elif compress:
    if identity:
        help_args(1)
    outfilename = os.path.join(btpath, basename)
    if indexed:
        infileglob = "%s-*.%s" % (basename, extension)
        btfile.compress_indexed(infileglob, outfilename, hex=hex)
    else:
        infilename = "%s.%s" % (basename, extension)
        btfile.compress(infilename, outfilename, hex=hex)
elif identity:
    if hex:
        help_args(2)
    inoutfilename = os.path.join(btpath, basename)
    if indexed:
        btfile.identity_recompress_indexed(inoutfilename)
    else:
        btfile.identity_recompress(inoutfilename)
else:
    help_args(1)


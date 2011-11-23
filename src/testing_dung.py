import os, sys

import bt.extract.btfile as btfile

res_path = os.path.join("..", "res")
msdos_bt1_path = os.path.join(res_path, "msdos", "bt1")

btfile.show_indexed_file_info("levs", msdos_bt1_path)
data = btfile.load_indexed_file("levs", msdos_bt1_path)

if len(sys.argv)>=2:
    levnum=int(sys.argv[1])
else:
    levnum=0

print levnum
print

lev1 = data[levnum]

#lev1=lev1[2:]

wall_data = lev1[0x0000:0x0200]
spec_data = lev1[0x0200:0x0400]

for i in xrange(22):
    for j in xrange(22):
        print "%02x" % wall_data[j+(21-i)*22], 
    print
print

for i in xrange(22):
    for j in xrange(22):
        print "%02x" % spec_data[j+(21-i)*22], 
    print
print

nmax = lev1[0x0400:0x0408]
print map(hex,nmax)

apar = lev1[0x0408:0x0410]
print map(hex,apar)

diff = lev1[0x0410]
print diff

phdo = lev1[0x0411]
print phdo

wstyle = lev1[0x0412]
print wstyle

entrypos = lev1[0x0413:0x0415]
print list(entrypos)

unknown = lev1[0x0415]
print unknown

dname = lev1[0x0416:0x0420]
#print "".join(map(lambda c: chr(c-0xC1+ord("A")),dname))

data = btfile.load_file("MEMDUMP.BIN", msdos_bt1_path)
start=0x000c4742
c64enc=data[start:start+256]
c64enc[0]="\n"
c64decode = lambda buf: "".join(chr(c64enc[c]) for c in buf)
print c64decode(dname)

spec_coord = lev1[0x0420:0x0430]
print list(spec_coord)
spec_prog = lev1[0x0430:0x0440]
print list(spec_prog)

anitimag_coord = lev1[0x0440:0x0460]
print list(anitimag_coord)

telefrom_coord = lev1[0x0460:0x0470]
print list(telefrom_coord)

teleto_coord = lev1[0x0470:0x0480]
print list(teleto_coord)

spinner_coord = lev1[0x0480:0x0490]
print list(spinner_coord)

smoke_coord = lev1[0x0490:0x04A0]
print list(smoke_coord)

hp_dam_coord = lev1[0x04A0:0x04C0]
print list(hp_dam_coord)

sp_rest_coord = lev1[0x04C0:0x04D0]
print list(sp_rest_coord)

stasis_coord = lev1[0x04D0:0x04E0]
print list(stasis_coord)

msg_coord = lev1[0x04E0:0x04F0]
print list(msg_coord)

encounter_coord = lev1[0x04F0:0x0500]
print list(encounter_coord)

encounter_num_type = lev1[0x0500:0x0510]
print list(encounter_num_type)

text_offset = lev1[0x0510:0x0520]
print list(text_offset)

texts = lev1[0x0520:]
texts = c64decode(texts)
#print texts
for i, text in enumerate(texts.split("\\")):
    if i<8 and msg_coord[2*i]<22 and msg_coord[2*i+1]<22:
        print ">", bytearray(text)



print "Done"

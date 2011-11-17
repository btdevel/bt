import bt.extract.bt1.data as dataload
import bt.extract.bt1.char as charload

res_path = "../res"
msdos_bt1_path = res_path + "/msdos/bt1"

dataload.load_classes(msdos_bt1_path)
dataload.load_races(msdos_bt1_path)


c1 = charload.load_msdos_character(4, msdos_bt1_path)

for f, v in sorted(c1.__dict__.items()):
    print f, v

print "\n\n\n"
c1.print_()

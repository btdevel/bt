tl=(159,79)
br=(383,255)


global last
last = None

from PIL import Image
def convert(x):
    global last
    file="orig/out-"+x+".png"
    im = Image.open(file)
    im=im.crop(tl+br)
    if last is None or list(im.getdata())!=list(last.getdata()):
        im.save("crop-"+x+".png")
        print "crop-"+x+".png"
    last=im

import glob
for x in sorted(glob.glob("orig/out-*.png")):
    print x[9:13]
    convert(x[9:13])
    

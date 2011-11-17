import os

def get_string_data(ba, ident, num):
    strings = [u"", ] * num
    start = ba.find(ident)
    for i in xrange(num):
        end = ba.find(b"\x00", start)
        strings[i] = str(ba[start:end])
        start = end + 1
    return strings

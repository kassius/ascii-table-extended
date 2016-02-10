#!/usr/bin/env python3.5

import unicodedata

#print('+----------+-----+-----+-----+--------------------------------------------+')
print('|   Binary | Dec | Oct | Hex | Code                                         |')
print('|----------|-----|-----|-----|----------------------------------------------|')
#print('+----------+-----+-----+-----+--------------------------------------------+')

names = []

for y in range(0,256):
    thisname = ""
    thisname = unicodedata.name(chr(y),"d3fault")
    if thisname != "d3fault":
        thisname = chr(y) + " " + thisname

    names.insert(y,thisname)

for x in range(0,256):
    print("| {0:08b} | {1:3d} | {2:03o} |  {3:02X} | {4:44s} |".format(x,x,x,x,names[x]))
#    print('+----------+-----+-----+-----+--------------------------------------------+')

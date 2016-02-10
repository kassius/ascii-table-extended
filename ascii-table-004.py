#!/usr/bin/env python3.5

import unicodedata

print('|   Binary | Decimal | Octal | Hexadecimal | Code                                         |')
print('|----------|---------|-------|-------------|----------------------------------------------|')

names = []

#mnames[7] = "BS - Backspace";

mnames = {
        0: "NUL",
        1: "SOH - START OF HEADING, CONSOLE INTERRUPT",
        2: "STX - START OF TEXT",
        3: "ETX - END OF TEXT",
        4: "EOT - END OF TRANSMISSION",
        5: "ENQ - ENQUIRY",
        6: "ACK - ACKNOWLEDGEMENT",
        7: "BEL - BELL",
        8: "BS - BACKSPACE",
        9: "HT - HORIZONTAL TAB",
        10: "LF - LINE FEED",
        11: "VT - VERTICAL TAB",
        12: "FF - FORM FEED",
        13: "CR - CARRIAGE RETURN",
        14: "SO - SHIFT OUT",
        15: "SI - SHIFT IN",
        16: "DLE - DATA LINK ESCAPE",
        17: "DC1 - DEVICE CONTROL 1 (OFT. XON)",
        18: "DC2 - DEVICE CONTROL 2" ,
        19: "DC3 - DEVICE CONTROL 3 (OFT. XOFF)",
        20: "DC4 - DEVICE CONTROL 4",
        21: "NAK - NEGATIVE ACKNOWLEDGMENT",
        22: "SYN - SYNCHRONOUS IDLE",
        23: "ETB - END OF TRANSMISSON BLOCK",
        24: "CAN - CANCEL",
        25: "EM - END OF MEDIUM",
        26: "SUB - SUBSTITUTE",
        27: "ESC - ESCAPE",
        28: "FS - FILE SEPARATOR",
        29: "GS - GROUP SEPARATOR",
        30: "RS - RECORD SEPARATOR",
        31: "US - UNIT SEPARATOR",

        127: "DEL - DELETE",
        }

for y in range(0,256):
    thisname = ""
    thisname = unicodedata.name(chr(y),"d3fault")

    if thisname != "d3fault":
        thisname = chr(y) + " " + thisname
    else:
        try:
            if mnames[y]:
                thisname = mnames[y]
        except:
            pass

    names.insert(y,thisname)

for x in range(0,256):
    print("| **{0:08b}** |     {1:3d} |   {2:03o} |          {3:02X} | {4:44s} |".format(x,x,x,x,names[x]))
#    print('+----------+-----+-----+-----+--------------------------------------------+')

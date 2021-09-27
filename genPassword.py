import random

def convertN2S(tc):#converts numbers(1-26) to the corresponding letter
    if(tc == 1):
        return "a"
    if(tc == 2):
        return "b"
    if(tc == 3):
        return "c"
    if(tc == 4):
        return "d"
    if(tc == 5):
        return "e"
    if(tc == 6):
        return "f"
    if(tc == 7):
        return "g"
    if(tc == 8):
        return "h"
    if(tc == 9):
        return "i"
    if(tc == 10):
        return "j"
    if(tc == 11):
        return "k"
    if(tc == 12):
        return "l"
    if(tc == 13):
        return "m"
    if(tc == 14):
        return "n"
    if(tc == 15):
        return "o"
    if(tc == 16):
        return "p"
    if(tc == 17):
        return "q"
    if(tc == 18):
        return "r"
    if(tc == 19):
        return "s"
    if(tc == 20):
        return "t"
    if(tc == 21):
        return "u"
    if(tc == 22):
        return "v"
    if(tc == 23):
        return "w"
    if(tc == 24):
        return "x"
    if(tc == 25):
        return "y"
    if(tc == 26):
        return "z"
    
def convertN2SY(tc):
    if(tc == 1):
        return "`"
    if(tc == 2):
        return "~"
    if(tc == 3):
        return "!"
    if(tc == 4):
        return "@"
    if(tc == 5):
        return "#"
    if(tc == 6):
        return "$"
    if(tc == 7):
        return "%"
    if(tc == 8):
        return "^"
    if(tc == 9):
        return "&"
    if(tc == 10):
        return "*"
    if(tc == 11):
        return "("
    if(tc == 12):
        return ")"
    if(tc == 13):
        return "-"
    if(tc == 14):
        return "_"
    if(tc == 15):
        return "+"
    if(tc == 16):
        return "="
    if(tc == 17):
        return "["
    if(tc == 18):
        return "{"
    if(tc == 19):
        return "]"
    if(tc == 20):
        return "}"
    if(tc == 21):
        return "\\"
    if(tc == 22):
        return "|"
    if(tc == 23):
        return ";"
    if(tc == 24):
        return ":"
    if(tc == 25):
        return "'"
    if(tc == 26):
        return '"'
    if(tc == 27):
        return "<"
    if(tc == 28):
        return ","
    if(tc == 29):
        return ">"
    if(tc == 30):
        return "."
    if(tc == 31):
        return "?"
    if(tc == 32):
        return '/'

def genPassword(length):#makes a password of the given length
    length1 = length - 1
    fullPass = []
    counter = 0
    while counter < length1:
        nos = random.randint(1, 3)
        if(nos == 1):
            n = random.randint(0,10)
            nsf = str(n)
            fullPass.append(nsf)
        if(nos == 2):
            s = random.randint(1,26)
            sc = convertN2S(s)
            sUOL = random.randint(1,2)
            if(sUOL == 1):
                fullPass.append(sc)
            else:
                fullPass.append(sc.upper())
        if(nos == 3):
            sy = random.randint(1,32)
            syc = convertN2SY(sy)
        counter += 1
    fullPassJ = "".join(fullPass)
    return fullPassJ
        

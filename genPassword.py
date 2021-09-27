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
    

def genPassword(length):#makes a password of the given length
    length1 = length - 1
    fullPass = []
    counter = 0
    while counter < length1:
        nos = random.randint(1, 2)
        if(nos == 1):
            n = random.randint(1,10)
            nsf = str(n)
            fullPass.append(nsf)
        if(nos == 2):
            s = random.randint(1,26)
            sc = convertN2S(s)
            fullPass.append(sc)
        counter += 1
    fullPassJ = "".join(fullPass)
    return fullPassJ
        

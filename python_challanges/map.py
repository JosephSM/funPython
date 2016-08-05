
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

other = "map"
def codetrans(str):
    translated = ""
    for i in str:
        if i in " .()'":
            translated += i
        elif i in "xyz":
            translated += chr(ord(i)%120+96)
        else:
            translated += chr((ord(i)+2))
    return(translated)


print(codetrans(str))
print(codetrans(other))
    

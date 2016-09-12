from pprint import pprint

message = "Hey what's up my name is Joe, how gooes it?"
charsdict = {}
for char in message:
    charsdict.setdefault(char, 0)
    charsdict[char] += 1

pprint(charsdict)
from pprint import pprint
dict = {}
with open("bigblockfile.txt") as file:
    for line in file:
        for char in line:
            dict.setdefault(char, 0)
            dict[char] += 1

pprint(dict)

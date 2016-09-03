import string

ABC = string.ascii_lowercase


def maketabe():
    transtabe = {}
    for i in range(len(ABC)):
        idx = i + 2
        trans_letter = ABC[idx % len(ABC)]
        transtabe[ABC[i]] = trans_letter
    return transtabe


def translate(sentence, transtable=maketabe()):
    newsentence = ""
    for let in sentence:
        if let in transtable:
            newsentence += str(transtable[let])
        else:
            newsentence += str(let)
    return newsentence

def longword(sentence):
    words = sentence.split(" ")
    longestWord = "i"
    for i in words:
        while len(longestWord) < len(words[i]):
            longestWord = words[i]
    return longestWord
        
longword("Hi my name is joey Schwartz")

import pprint

number = 1
last = 0
beforelast = 0
sequence = []

while number <= 4000000:
    beforelast = last
    last = number
    number = last + beforelast
    if number%2 == 0:
        print number
        sequence.append(number)
    else:
        print number
        

pprint.pprint(sequence)
print(sum(sequence))

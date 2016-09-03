import math


def primefctsof(num):
    fcpr = getfctpair(num)
    if not fcpr:
        return [num]
    return primefctsof(fcpr[0]) + primefctsof(fcpr[1])


def getfctpair(num):
    start = int(math.sqrt(num))
    for i in range(start, 1, -1):
        if num % i == 0:
            return [i, num//i]
    return []


def isprime(num):
    return not bool(getfctpair(num))

for i in range(2, 100):
    print(i, isprime(i), getfctpair(i) if getfctpair(i) else "[prime]", primefctsof(i))


# print(primefctsof(100000))
# check = 1
# for i in mainlist:
# 	check *= i
# print('check is,',check)


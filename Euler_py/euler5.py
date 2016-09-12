def evenlyDivisible(n1 , n2):
    return n1%n2 == 0

def numgen():
    n = 2520
    while(True):
        yield n
        n += 2520

g = numgen()
list = range(20, 10, -1)
def solution():
    for i in g:
        if(all([evenlyDivisible(i, n) for n in list])):
            return(i)

print(solution())


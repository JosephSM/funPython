# what is the largest prime factor of 600851475143??

from math import sqrt

def largestfactors(n):
    uptonum = int(sqrt(n))
    cleaned = [i for i in range(2, uptonum) if n % i == 0]
    return [x for x in cleaned if x%2 != 0]

def isPrime(n):
    for i in range(2, n):
        if(n%i == 0):
            return False
    return True


pool = largestfactors(600851475143)
final = list(filter(isPrime, pool))
print(final)

assert(isPrime(13) == True)
assert(isPrime(37) == True)
assert(isPrime(9) == False)
assert(isPrime(15) == False)

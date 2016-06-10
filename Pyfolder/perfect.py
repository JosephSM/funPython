from math import sqrt


def isPerfect(n):
    return n == sum(factors(n))


def factors(n):
    fs = {1}
    for i in xrange(2, int(sqrt(n) + 1)):
        if n % i == 0:
            fs.add(i)
            fs.add(n / i)
    return fs


def perfect_up_to(upper):
    up_to = []
    for number in xrange(2, upper):
        if isPerfect(number):
            up_to.append(number)
    return up_to


def perfects():
    number = 2
    while True:
        if isPerfect(number):
            yield number
        number += 1


def paginate(data, page_size=2):
    page = []
    for x in data:
        page.append(x)
        if len(page) == page_size:
            yield page
            page = []
    if len(page) != 0:
        yield page

# assert(isPerfect(6))
# assert(isPerfect(7) == False)
# assert(factors(6) == set([1,2,3]))
# assert(factors(9) == set([1,3]))




# print perfect_up_to(2000000)

            







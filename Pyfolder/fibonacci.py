def fibonacci(num):
    list = []
    first = 0
    second = 1
    for i in range(num):
        list.append(first)
        new = first + second
        first = second
        second = new    
    return list


def recfib(n):
    if n == 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return recfib(n-1) + recfib(n-2)


def recfiblist(s):
    if s == 0:
        return []
    return recfiblist(s-1) + [recfib(s)]

print([]+[recfib(1)]+[recfib(2)]+[recfib(3)]+[recfib(4)]+[recfib(5)])

#Three ways to print the fibonacci sequence

print(recfiblist(10))

# fibs = []
# for i in range(1,31):
#     fibs.append(recfib(i))
# print(fibs)

# print(recfib(10))


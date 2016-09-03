from operator import mul
from functools import reduce
list = [[x, y] for x in range(999, 99, -1) for y in range(999, 99, -1)]
l2 = [reduce(mul, i) for i in list]
print(max([n for n in l2 if(str(n) == str(n)[::-1])]))
    

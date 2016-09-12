import random

sum = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

newList = []
for i in range(0, 20):
    newList.append(random.randint(0, 100))
    i += 1
    
print(newList)
print(len(newList))

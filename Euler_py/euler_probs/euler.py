#sum of all natural numbers that are multiples of 3 or 5 below 1000
#Euler Problem #1 -
number = 0
for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        number += i
    else:
        continue
print('Euler #1 =',number)
print('################################################\n')


#Euler problem #2
##Fibonacci sequence whose values do not exceed four million,
##find sum of even valued terms

f = 0
s = 1
t = 0
ans = []
sum = 0
while t < 4000000:
    t = f + s
    f = s
    s = t
### print('this is fib', f)
    if s%2 == 0:
#        print('this is even fib', s)
        ans.append(s)
#print (ans)

for i in range(0,len(ans)):
    sum += ans[i]
print("Euler #2 = ",sum)

print("##############################################\n")
print("Euler #3")
# Largest Prime Factor of 600851475143?

import math
#GPF 600851475143

bilnum = 600851475143
pairs = math.floor(math.sqrt(bilnum))
print(pairs)
slist = []
for i in range(pairs,0,-1):
	if bilnum%i == 0:
		slist.append(math.floor(i))
		slist.append(math.floor(bilnum/i))
print(slist)
nlist = []
for i in range(0,len(slist), +2):
	nlist.append(math.floor(slist[i]*slist[i+1]))
#print (nlist)


##
for i in range(len(slist)):
	num = math.floor(math.sqrt(slist[i]))
	if slist[i]%num != 0: 
		num-=1
	


	


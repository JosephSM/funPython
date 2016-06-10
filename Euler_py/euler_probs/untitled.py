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
	


	


arr = [10,10,10,4,10,10,10]
arr2 = [1,2,3,4,2,4,2,4,5,6,7,5,3,5,6,7,4,3,3,6,6,3,3,4,5,6,43,24,5,53]
def equil(arr):
    for i, num in enumerate(arr[:]):
        if(sum(arr[:i])==sum(arr[i+1:])):
            return(i)


sumb4 = 0
sumafta = sum(arr[1:])
for i in range(1, len(arr)-1):
    sumb4 += arr[i-1]
    sumafta -= arr[i]
    if(sumb4==sumafta):
        print(i)

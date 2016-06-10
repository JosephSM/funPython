def fibbonacci(number):
    if(number==0):
        return 0
    elif(number==1):
        return 1
    else:
        return 1+fibbonacci(number-1)


fibbonacci(3)

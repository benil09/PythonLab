# Write a python script to print the first n terms of the Fibonacci series using while loop

def fibbonacciSeries(n):
    i=0
    firstNum=0
    secondNum=1
    while i<n:
        print(firstNum,end=" ")
        temp=firstNum
        firstNum=secondNum
        secondNum=temp+secondNum
        i+=1
    return 

print (fibbonacciSeries(5))

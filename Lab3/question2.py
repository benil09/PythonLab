# Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.


def sumOfDigits(n):
    sum = 0
    while n>0:
     rem=n%10
     sum+=rem
     n= int (n/10)
    return sum



print( sumOfDigits(154)  )
  

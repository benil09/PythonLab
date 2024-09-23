#Calculate the area of trinagle and angle between the  sides if its sides are given

import math
a=int (input("enter the value of side 1:"))
b=int (input("enter the value of side 2:"))
c=int (input("enter the value of side 3:"))

S=(a+b+c)/2
A=math.sqrt(S* (S-a)*(S-b)*(S-c))
print("the area of triange is :", A)


#angle calculation

angleA=(b**2 + c**2 - a**2)/2*a*b
angle=math.cos(angleA)
print(angle)











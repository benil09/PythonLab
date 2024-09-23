# Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

def table(n):
    limit = int(input("Enter the limit: "))
    
    for i in range(1,limit+1):
        print(f"{n} * {i} = {n*i}")
        
    return


print(table(5))
        

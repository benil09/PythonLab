# Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for. Print True if all characters are alphanumeric. Otherwise print False.




def checkAlphaNumeric(s):
    for char in s:
        if not char.isalnum():
            return False
    return True

string=input("enter a string")
if checkAlphaNumeric(string):
    print("True")
else:
    print("False")
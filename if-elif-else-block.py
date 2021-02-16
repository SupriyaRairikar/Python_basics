"""
if(expression):
    statement
"""
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
if(n1 > n2):
    print("{} is greater than {}".format(n1,n2))
elif(n1 == n2):
    print("{} is equal to {}".format(n1,n2))
else:
    print("{} is greater than {}".format(n2,n1))
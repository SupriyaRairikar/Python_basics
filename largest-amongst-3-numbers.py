n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))
if(n1 > n2 & n1 > n3 ):
    print("{} is greater than {} and {}".format(n1,n2,n3))
elif(n2 > n3):
    print("{} is greater than  {} and {}".format(n2,n1,n3))
else:
    print("{} is greater than  {} and {}".format(n3,n1,n2))
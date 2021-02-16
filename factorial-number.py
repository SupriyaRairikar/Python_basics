num = int(input("Enter the number to get factorial : "))
fact = 1
for count in range(1,num+1):
    fact=fact*count
print("Factorial of {} is {} \n successful !!!".format(num,fact))
def addtwoNumbers(n1,n2):
    return n1+n2

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

result = addtwoNumbers(num1,num2)
print("sum of {} and {} is {}".format(num1,num2,result))
"""
__name__

this is special variable in python
that holds the name of currnt python program

We can use python program in two ways :
1. Standalone python program
2. use of python program in some other program as a module

whenever we run python program the value of __name__ gets set as __main__

"""

def Sum_numbers(a1,a2):
    result = a1+a2
    print("{} + {} = {} ".format(a1,a2,result))
batch_name="DESD_FEB_2020"

if __name__  == "__main__":
     num1=int(input("Enter number 1 : "))
     num2=int(input("Enter number 2 : "))
     Sum_numbers(num1,num2)
     print("__name__ gets executed : value is :",__name__)
else:
     print("Program is imported in some other file")

print("__name__ gets executed : value is :",__name__)
print("hello world")
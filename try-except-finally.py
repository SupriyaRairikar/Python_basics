"""
finally block gets executed whenever there is no exception
"""

def div(n1,n2):
    return n1/n2
try:
    n1=int(input("Enter the number 1 : "))
    n2=int(input("Enter the number 2 : "))
    result = div(n1,n2)
    print("{} / {} = {}".format(n1,n2,result))
except :
    print("number 2 must be grater than 0\n----invalid input-----\n")
finally:
    print("division operation is done-----")
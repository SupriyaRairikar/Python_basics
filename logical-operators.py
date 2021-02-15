"""
and-----true if both operands r true
or---------true if either of the operatoris true
not------true if operand is false
"""
x=True #boolean type
y=False
z=True

res1=x and y
res2=x and z
res3=not y
res4= x or y
res5= y or z

print("{0} and {1} is {2}".format(x,y,res1))
print("{0} and {1} is {2}".format(x,z,res2))
print("not of {0} is {1}".format(y,res3))
print("{0} or {1} is {2}".format(x,y,res4))
print("{0} or {1} is {2}".format(y,z,res5))
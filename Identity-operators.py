"""
is - true if operands are identical(refers to same object)
is not-true if operands are not identical-----do not refer same object
"""
x=5
y=5
z=10
#x,y is stored in stack
# valueis stored in heap

location_x=id(x)
location_y=id(y)
location_z=id(z)

print("value of x is stored at: ",location_x)
print("value of y is stored at: ",location_y)
print("value of {0} is stored at {1}".format(z,location_z))

res= x is y
print("x is y =",res)
res1= x is z
print("x is z =",res1)

n1=-5
n2=-5
print("n1 is n2 =",n1 is n2)

s1='hi'
s2='hi'
print("s1 is s2 =",s1 is s2)
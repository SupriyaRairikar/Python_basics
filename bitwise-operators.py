"""
&----bitwise and
| ------bitwise or
~ -----bitwise not
^ -----bitwise xor
>> -----bitwise right shift
<< -----bitwise left shift

"""
n1=10 #00001010
n2=7    #00000111
n3=2

res=n1 & n2
res1=n1 | n2
res2=n1 ^ n2
res3=n1 >> n3
res4=n2 << n3

print("{0} & {1} is {2}".format(n1,n2,res))
print("{0} | {1} is {2}".format(n1,n2,res1))
print("{0} ^ {1} is {2}".format(n1,n2,res2))
print("{0} ^ {1} is {2}".format(n1,n3,res3))
print("{0} ^ {1} is {2}".format(n2,n3,res4))

#set nth bit of a number
#que-----set the first bit of numbe 10
#formula----(1 << nth bit) | number
val= ((1 << 3) | 10)
print(val)
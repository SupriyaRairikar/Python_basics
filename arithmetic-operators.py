"""
Arithmetic operations-----
+ - unary plus
-unary minus
* multiplication
/ division resultwill be in float---float division
% modulus
// floor division---results in whole number
** exponential
"""
num1=10
num2=6
sum= num1 + num2
sub= num1 - num2
mul= num1 * num2
floatDiv= num1 /num2
modulusNum= num1 % num2
floorDiv= num1 // num2
expo = num1 ** num2

#format function 10+6=16 (num1+num2=sum)

print("{0} + {1} = {2}".format(num1,num2,sum))
print("{0} - {1} = {2}".format(num1,num2,sub))
print("{0} * {1} = {2}".format(num1,num2,mul))
print("{0} / {1} = {2}".format(num1,num2,floatDiv))
print("{0} % {1} = {2}".format(num1,num2,modulusNum))
print("{0} // {1} = {2}".format(num1,num2,floorDiv))
print("{0} ** {1} = {2}".format(num1,num2,expo))

cal=(3+4*5)
print("value of cal is ",cal)

cal1=(3+4*5//5-10)
print("value of cal is ",cal1)
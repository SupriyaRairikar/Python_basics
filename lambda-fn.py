"""
lambda arguments : expression
"""

result = lambda a,b : a+b

print("sum = {}".format(result(10,5)))

mul= lambda n1,n2,n3 : n1*n2*n3
res = mul(10,5,5)
print("mltiplication = {}".format(res))
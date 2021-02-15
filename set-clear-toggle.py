"""
set, clear and toggle a given bit of a number in python


"""
number =5
bit = 1

#set a bit
res1 = (number | (1 << (bit-1)))
print(res1)

#clearing a bit
res2 = (number & ~(1 << (bit-1)))
print(res2)

#toggle a bit
res3 = (number ^ (1 << (bit-1)))
print(res3)
#local scope
def printNum():
    number = 10
    print(number) #---local scope
printNum()
#print(number)----error---numbr is not defined

x=100
def testfun():
    print(x)

testfun()    
print(x) #-----global scope
x+=1
print(x)

def function3():
    global value
    value=500   #local value declared as global
    print(value)

function3()
print(value)  #value is accessible outside the fn   
value+=1
print(value) 

del function3 #delete a fn
#function3()  #------- after calling again gives error----fn not defined
num = 0
while(num < 5):
    num+=1
    if(num==3):
        pass #---dummy statement------it will not execute the loop---
        #directly passesthe control to next statement
        #whenever syntactical requirement need to be filled
        #without assignment of any opertion
    else:
        print("count : {} ".format(num))

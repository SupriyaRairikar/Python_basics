"""
0 - sunday
1 - monday
2
3
4.........
"""

def sunday():
    return "today is sunday"
def monday():
    return "today is monday"
def tuesday():
    return "today is tuesday"
def wednesday():
    return "today is wednesday"
def thursday():
    return "today is thursday"
def friday():
    return "today is friday"
def saturday():
    return "today is saturday"
def default():
    return "please enter the day"

switch_days=\
    { #dictionary

        0 : sunday(),
        1 : monday(),
        2 : tuesday(),
        3 : wednesday(),
        4 : thursday(),
        5 : friday(),
        6 : saturday()

    }   
def printdays(daysofweek):
    return(switch_days.get(daysofweek,default()))
while True:
    input_days=int(input("enter the days of week-----"))
    print(printdays(input_days))
    if(input_days == 10):
        break
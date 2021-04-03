student_list = ["sdr","suraj", "sarmad", "meera"]
print("the students are : ")
for st in student_list :
    print(st,end=(" "))
print("\n")

name = input("Enter your name : ")
for student in student_list:
    if(name == student ):
        print("Entry allowed------")
        break
    else:
        print("Entry not allowed Contact CC")

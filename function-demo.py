"""
def function_name:
    statements:
function_name() ##calling the fn
"""
def Helloworld():
    print("hello world in python .....")
Helloworld()

def Student_details(name,branch):
    print("name of the student is : {}".format(name))
    print("Branch of the student is : {}".format(branch))
    print("congrtulations your details are verified......")

Student_name = input("Enter the name : ")
Student_branch = input("Enter the branch : ")
Student_details(Student_name,Student_branch)
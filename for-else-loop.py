for num in range(1,11) :
    print(num,end=(" "))
else:
    print("\n")
    print("Your data is ready")

#you want the user to allow to enter password 3 times
saved_password = "desd"
for times in range(3):
    password = input("\nenter your password : ")
    if(password ==saved_password saved_password):
        print("login successful !!!")
        break
else:
     print("you have completed the limit to enter the incorrect password!! \
          \n try again with correct password")
       


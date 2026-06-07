username = input("Enter your username :")
password = input("Enter your password :")

if username == "admin" :
    if password == "admin":
        print("successful login")
    else:
        print("incorrect password")

else:
    print("user not found")




reg_password = "W5777"
authorized = False

while authorized != True:
    user_input = input("enter your password: ")
    if user_input == reg_password:
        print("access granted")
        authorized = True
    else:
        print("password incorrect try again")
    
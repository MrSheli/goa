pin = 506
authorized = False

while authorized != True:
    user = int(input("enter your pin: "))

    if user == pin:
        print("access granted")
        authorized = True
    else:
        print("try again")

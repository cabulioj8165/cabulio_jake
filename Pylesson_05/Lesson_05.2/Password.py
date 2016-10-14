uname = "Jake"
pword = "idk"

def passCheck():
    uname = input("Enter the username: ")
    pword = input("Enter the password: ")
    if uname != "Jake":
        if pword != "idk":
            print("Both your username and password are incorrect! ")
            passCheck()
    if uname != "Jake":
        if pword == "idk":
            print("The user name is incorrect! ")
            passCheck()
    elif uname == "Jake":
        if pword == "idk":
            print("Correct. Access granted! ")
        else:
            print("The password is incorrect! ")
            passCheck()

passCheck()

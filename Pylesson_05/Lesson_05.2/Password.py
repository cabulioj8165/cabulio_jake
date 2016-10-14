<<<<<<< HEAD
uname = "Jake"
pword = "idk"
=======
uname = "JakeCabulio"
pword = "TheGreatest"
>>>>>>> origin/master

def passCheck():
    uname = input("Enter the username: ")
    pword = input("Enter the password: ")
<<<<<<< HEAD
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
=======
    if uname != "JakeCabulio":
        if pword != "TheGreatest":
            print("Both your username and password are incorrect! ")
    if uname != "JakeCabulio":
        if pword == "TheGreatest":
            print("The user name is incorrect! ")
    elif uname == "JakeCabulio":
        if pword == "TheGreatest":
            print("Correct. Access granted! ")
        else:
            print("The password is incorrect! ")
>>>>>>> origin/master

passCheck()

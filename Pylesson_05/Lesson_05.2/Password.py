uname = "JakeCabulio"
pword = "TheGreatest"

def passCheck():
    uname = input("Enter the username: ")
    pword = input("Enter the password: ")
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

passCheck()

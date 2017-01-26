import random

class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 100000000)

    def setAvatar(self, newAvatar):
        self.avatar = newAvatar

    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getUserName(self):
        return self.userName
    def getAvatar(self):
        return self.avatar

def main():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    avatar = ""
    
    user1 = User(firstName, lastName, avatar)

    askAvatar = input("Would you like to use a public avatar? (y or n): ")
 
    if askAvatar == "y":
          avatarName = input("Enter the name of your avatar: ")
          avatar = avatarName
          user1 = User(firstName, lastName, avatar)
    elif askAvatar == "n":
         user1 = User(firstName, lastName)

    def __str__(user1):
        if askAvatar == "y":
            return "Customer Info...\nFirst Name: " + user1.firstName + "\nLast Name: " + user1.lastName + "\nAvatar: " + user1.avatar + "\nUser ID#: " + str(user1.userID)
        elif askAvatar == "n":
            return "Customer Info...\nFirst Name: " + user1.firstName + "\nLast Name: " + user1.lastName + "\nUser ID#: " + str(user1.userID)
    print(__str__(user1))
main()

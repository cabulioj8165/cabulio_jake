import time

def gameStart():
    gameStart = input("This is an adventure game. Tap of Y to play or N if you don't want to. ")
    if gameStart == "Y" or gameStart == "N":
       if gameStart == "Y":
           print("Okay, great! Let's get started! ")
           time.sleep(.5)
           fname = input("Let's first ask for your name? ")
           time.sleep(.5)
           age = input("Hey " + fname + ". How old are you? ")
           if age < 14:
               print("Oh... you are too young to play this game. ")
           else:
               print("Okay, great! ")
       else:
            print("Aww that sucks!")
gameStart()

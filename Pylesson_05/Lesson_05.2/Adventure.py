import time

def gameStart():
    gameStart = input("This is an adventure game. Tap of Y to play or N if you don't want to. ")
    if gameStart == "Y":
       if gameStart == "Y":
           print("Okay, great! Let's get started! ")
           time.sleep(.5)
           fname = input("Let's first ask for your name? ")
           time.sleep(.5)
           age = int(input("Hey " + fname + ". How old are you? "))
           if age <= 13:
               print("Oh... you are too young to play this game. ")
           else:
               print("Okay, great! ")
               print("Let's move on to the first day!")
               time.sleep(1)
               print("________________________________________")
               print("                Day 1                   ")
               print("\n")
               time.sleep(1)
               print("location: hospital")
               time.sleep(1)
               print("Citizen: Ahhhhhhhhhh! Runnnn! They are COMING!!!!!")
               time.sleep(.5)
               run = input("*Do you want to: run or stay?* ")
               if run == "run":
                   print("Citizen: Okay then, let's goooo! ")
                   time.sleep(2)
                   print("*You run with the citizens in the hospital, hoping to survive.* ")
                   time.sleep(2)
                   print("When suddenly... ")
                   time.sleep(2)
                   print("Citizen: AHHHHHHHH! They are right there!!!!! ")
                   time.sleep(1.5)
                   print("*There are zombies right around the corner.* ")
                   time.sleep(2.5)
                   print("You decide to leave the group and attack the zombies. ")
                   time.sleep(2)
                   print("Citizen: Here, take this. You will need it. ")
                   time.sleep(2)
                   print("*The citizen gives you a steel machete to use for battle.* ")
                   time.sleep(1.5)
                   print("*Okay, now you are alone with a steel machete ")
                   print("There are 7 zombies.* ")
                   time.sleep(3)
                   sneek = input("*Would you like to: sneek from behind or attack head on?* ")
                   if sneek == "sneek from behind":
                       time.sleep(1)
                       print("*You have successfully taken out the zombies.* ")
                       time.sleep(.5)
                       goWhere = input("Do you want to: find the citizens or head on without them? ")
                       if goWhere == "find the citizens":
                           time.sleep(.5)
                           print("*You head off to find the citizens ")
                           print("and you see a zombie with a sword.* ")
                           time.sleep(1)
                           print("*The zombie throws a swing at you.* ")
                           dodge = input("*Do you want to: try to stab him or dodge the swing?* ")
                           if dodge == "dodge the swing":
<<<<<<< HEAD
                               time.sleep(
                                   1)
=======
                               time.sleep(1)
>>>>>>> origin/master
                               print("*You have successfully dodged the zombie's attack.* ")
                               time.sleep(1)
                               print("*What attack move do you want to do: ")
                               attackMove = input("stab in stomach or go for head?* ")
                               if attackMove == "stab in stomach":
                                   time.sleep(.5)
                                   print("*You killed the zombie!* ")
                                   time.sleep(2)
                                   print("*It is getting late. You decide to set up camp ")
                                   print("in a trailor next to the hospital* ")
                                   time.sleep(2)
                                   print("You have successfully completed day 1! ")
                                   time.sleep(2)
                                   print("\n")
                                   print("________________________________________")
                                   print("                Day 2                   ")
                                   time.sleep(1)
                                   print("Coming soon... ")
                               else:
                                   time.sleep(.5)
                                   print("*You swing your machete towards his head ")
                                   print("and miss. He then kills you with his sword. ")
                                   time.sleep(2)
                                   print("Game Over...")
                           else:
                               time.sleep(1)
                               print("*You try to stab him in the stomach but ")
                               print("he severes your face off and you die.* ")
                               time.sleep(.5)
                               print("Game Over. ")
                       else:
                            print("*You travel to find the citizens but then a ")
<<<<<<< HEAD
=======
                            time.sleep(1)
>>>>>>> origin/master
                            print("boulder breaks the wall and smashes you.*")
                            time.sleep(1)
                            print("*You survive it but your legs are smashed so you can't move* ")
                            time.sleep(1)
                            print("*You slowly and painfully die off.* ")
                            time.sleep(2)
                            print("Game Over...")
                   else:
                       print("*You stab one zombie in the head and another in the stomach but the rest is ")
                       print("history.* ")
                       time.sleep(1)
                       print("Game over. ")
               else:
                  print("Citizen: Okay then, I guess you will die off with the rest... see ya!")
                  time.sleep(1)
                  print("*You eventually die off with no weapons with you.* ")
                  time.sleep(1)
                  print("Game Over...")
    else:
        print("Aww that sucks!")

gameStart()

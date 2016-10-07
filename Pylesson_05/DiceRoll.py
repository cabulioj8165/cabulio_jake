import random
import time

replay = 1
print("This is a dice roll game.")
print("The person with the highest score wins.")
enter = input("Press enter for the numbers.")
amountTime = input("The numbers will appear in three seconds. Press enter to begin timer.")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
num1 = random.randint(1 , 7)
num2 = random.randint(1 , 7)
print("Your number is:" , num1)
time.sleep(1)
print("The computer's number is:" , num2)

if num1 > num2:
    time.sleep(1)
    print("You win!")
elif num1 < num2:
    time.sleep(1)
    print("You lose! Better luck next time! ")
elif num1 == num2:
    time.sleep(1)
    print("It is a tie!")
time.sleep(.5)
y = int(input("Do you like this game? Please rate from 1-10."))

if y < 5:
    print("Come on, it was better than that! ")
elif y > 5:
    print("Thank you for the rate! ")

replay = input("Do you want to play again? 1 for yes, 2 for no. ")

if replay == 1:
    print("Okay, great! ")
    replay
elif replay == 2:
    print("Okay, see you later! ")

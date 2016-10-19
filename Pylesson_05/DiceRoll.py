import random
import time

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

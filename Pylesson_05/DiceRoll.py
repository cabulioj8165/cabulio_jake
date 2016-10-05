import random

print("This is a dice roll game.")
print("The person with the highest score wins.")
enter = input("Press enter for the numbers.")


num1 = random.randint(1 , 7)
num2 = random.randint(1 , 7)
print("Your number is:" , num1)
print("The computer's number is:" , num2)

if num1 > num2:
    print("You win!")
if num1 < num2:
    print("You lose! Better luck next time! ")

y = int(input("Do you like this game? Please rate from 1-10."))


if y < 5:
    print("Come on, it was better than that! ")
if y > 5:
    print("Thank you for the rate! ")


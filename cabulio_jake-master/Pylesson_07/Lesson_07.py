number = int(input("Please enter a number: "))

while number > 0:
# %10 returns the last digit on the right
    print(number % 10)
# dividing by 10 shaves off the last digit on the right
    number = int(number / 10)

number = int(input("Please enter a number: "))
digits = 0
num = number

while num > 0:
    digits += 1
    num = int(num / 10)


print("There are", digits, "digits in ", number)

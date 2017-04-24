import time

start = input("this is a bmi calculator. Press enter.")
weight = float(input("Please enter what you weigh in pounds. "))
height = float(input("Please enter your height in inches. "))

bmi = 0
bmi = (weight/(height*height))*703

condition = ("Undefined")

def calcBMI(bmi, condition):
    return bmi
if bmi < 18.5:
    condition = ("Underweight")
elif bmi < 24.9:
    condition = ("Normal")
elif bmi < 29.9:
    condition = ("Overweight")
elif bmi < 34.9:
    condition = ("Obese")
elif bmi < 39.9:
    condition = ("Very Obese")
elif bmi > 39.9:
    condition = ("Morbidly Obese")

time.sleep(.5)
print("One second")
time.sleep(2)
print("{}{}{}{:0.2f}{}".format("You are considered " , condition, ". Your bmi is " , bmi , ". " ))

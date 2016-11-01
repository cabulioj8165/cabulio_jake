number = int(input(" Please enter a number: "))

digits = 0
average = 0
num = number
while num > 0:
    digits += 1
    average += num % 10
    num = int(num / 10)
average = average/digits
print("The average of the digits in" , number , "is" , average)

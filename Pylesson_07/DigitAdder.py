number = int(input(" Please enter a number: "))

sum = 0
num = number
while num > 0:
    sum += 1
    num = int(num / 10)
print("The sum of the digits in" , number , "is" , sum)

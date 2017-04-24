number = int(input(" Please enter a number: "))

num = number
rev = 0
while num > 0:
    rev *= 10
    rev += num % 10
    num = int(num / 10)
print(number , "reversed is" , rev)

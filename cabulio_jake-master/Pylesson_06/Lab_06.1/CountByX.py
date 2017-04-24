num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
output = ""

for i in range(num1, num2 + 2, 2):
    output = output + str(i) + "    "
print(output)

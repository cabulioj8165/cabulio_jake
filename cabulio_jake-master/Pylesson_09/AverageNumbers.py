import random
numbers = []

for i in range(0, 10):
    numbers.append(random.randrange(1, 101))

output = ""
for i in range(0, len(numbers)):
    output += str(numbers[i]) + " "
def average():
    average = 0
    for i in range(0, len(numbers)):
        average += numbers[i]
    return average/len(numbers)

print("Numbers...")
print(output)
print("\n")
print("The average of the above number is... ")
print(average())

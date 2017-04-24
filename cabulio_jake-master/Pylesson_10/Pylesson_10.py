values = []
values.append([1, 2, 3, 4])
values.append([5, 6, 7, 8])
values.append([9, 10, 11, 12])
values.append([13, 14, 15, 16])


#print(values)
#print(values[2][1])

print("\nHere is what a list of lists looks like...")
print(values, "\n")
print("Using range...")
for i in range(0, len(values)): #outer loop: columns
    output = ""
    for j in range(0, len(values[i])): #inner loop: rows
        output += str(values[i][j]) + "\t"
    print(output + "\n")

print("Using enhanced loop...")
for value in values:
    output = ""
    for num in value:
        output += str(num) + "\t"
    print(output)

print("\nSeach the list...")
count = ""
for value in values:
    for number in value:
        if number % 5 == 0:
            count += str(number) + ", "
print("The numbers " + count + " in the list are multiples of 5. \n\n")

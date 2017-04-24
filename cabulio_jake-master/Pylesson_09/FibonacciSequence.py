start = int(input("Please enter your starting number: "))
size = int(input("Please enter your sequence size: "))
word = ""
seq = []

for i in range(0, size):
    if i == 0 or i == 1:
        seq.append(start)
    else:
        seq.append(seq[i - 1]+ seq[i - 2])
    word += str(seq[i]) + " "

print("The fibonacci sequence... ")
print(word)

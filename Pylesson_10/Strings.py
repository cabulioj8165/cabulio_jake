go = input("Please enter 16 strings: ")
splist = go.split()
wordsList = []
spot = 0
output = ""
for i in range(0,4):
    output += "\n"
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(splist[spot])
        output += wordsList[i][j] + "\t"
        spot+= 1
print(output)

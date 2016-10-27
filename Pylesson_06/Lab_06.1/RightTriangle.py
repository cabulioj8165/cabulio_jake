word = input("Please enter a word: ")

def RightTri(wrd):
    for i in range(len(wrd)+1, 0, -1):
        print(wrd[i:len(wrd)])
RightTri(word)

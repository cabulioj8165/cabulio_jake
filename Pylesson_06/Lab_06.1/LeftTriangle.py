word = input("Please enter a word: ")

def LeftTri(wrd):
    for i in range(0, len(wrd), 1):
        print(wrd[i:len(wrd)])
LeftTri(word)

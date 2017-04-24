word = input("Please enter a word: ")

def RevTri(wrd):
    for i in range(len(wrd), 0, -1):
        print(wrd[0:i])
RevTri(word)

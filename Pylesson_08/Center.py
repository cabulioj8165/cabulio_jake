words = input("Please enter 3 words: ")

def makeCenter():
    if len(words) >= 20:
        return words
    else:
        return makeCenter(" " + words + " ")
print(words)

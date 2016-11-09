word1 = input("Please enter a word: ")
word2 = input("Please enter another word: ")
word3 = input("Please enter another word: ")


def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        return makeCenter(" " + word + " ")

makeCenter(word1)
makeCenter(word2)
makeCenter(word3)

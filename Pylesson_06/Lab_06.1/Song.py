word1 = "Na"
word2 = "Hey"
word3 = "Goodbye!"
def Line(word1, word2, word3):
    for i in range(len(word1)):
        word1 = word1 + " "
        print(word1)
    for i in range(len(word2)-2):
        word2 = word2 + " "
        print(word2 + word2 + word2)
    for i in range(len(word3)-7):
        word3 = word3 + " "
        print(word3)
        print("Do you know the song? ")
Line(word1, word2, word3)

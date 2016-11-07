word = input("Please enter a word: ")

def wordBox(word, num):
   if(num >= len(word)):
       return ""
   else:
       print(word)
       wordBox(word, num + 1)

wordBox(word, 0)

word = input("Please enter a word: ")

start = ""
stop = len(word)

def tree(word, start, stop):
    if start <= 0:
        print(str(0 , start))
        start = start + 1
tree(word, start, stop)

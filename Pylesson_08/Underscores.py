sentence = input("Please enter a sentence: ")

top = 0
while top < sentence.count(" ") > 0:
    sentence = sentence[0 : sentence.index(" ")]  + "_" + sentence[sentence.index(" ")+1 : len(sentence)]

print(sentence)

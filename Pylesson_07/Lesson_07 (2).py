sentence = input("Please enter a String: ")

top = 0
while top < len(sentence):
    print(sentence[top])
    top +=1

sentence = input("Please enter a String: ")

top = 0
while top < sentence.count(" ") > 0:
    sentence = sentence[0 : sentence.index(" ")] + sentence[sentence.index(" ")+1 : len(sentence)]

print("Without spaces..." + sentence)

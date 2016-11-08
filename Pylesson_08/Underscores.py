sentence = input("Please enter a sentence: ")

top = 0
def replace(top, sentence):
    if top < len(sentence):
        if sentence.count(" ") < 1:
            sentence = sentence
        elif sentence.index(" ") > 1:
            while top < sentence.count(" ") > 0:
                sentence = sentence[0 : sentence.index(" ")]  + "_" + sentence[sentence.index(" ")+1 : len(sentence)]
    print(sentence)

replace(top, sentence)

def printf(word, number):
    print("{:<6}\t{:10.4f}".format(word, number))


word = "blah!"
number = 69789.312

printf(word, number)

word = "ohboy!"
number = 8879653.24858

printf(word, number)

num1 = float(input("What is average 1: "))
num2 = float(input("What is average 2: "))
num3 = float(input("What is average 3: "))
average = 0

def Average():
    global average, num1, num2, num3
    average = (num1 + num2 + num3)/3
def averagePrint():
    global average
    print("The average is {:.5f}".format(average))
    print("The average of " , num1 , "," , num2 , ", and" , num3 , "is {:.5f}".format(average))

Average()
averagePrint()

num1 = float(input("What is average 1: "))
num2 = float(input("What is average 2: "))
num3 = float(input("What is average 3: "))

def Average():
    global average
    average = (num1 + num2 + num3)/3
def averagePrint():
    print("The average of " , num1 , "," , num2 , ", and" , num3 , "is {:.5f}".format(average))

Average()
averagePrint()

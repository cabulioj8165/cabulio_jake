def Average():
    global num1, num2, num3
    num1 = float(input("Enter the first average: "))
    num2 = float(input("Enter the second average: "))
    num3 = float(input("Enter the third average: "))

def calcAverage():
    print ("The average of the three numbers are" , (num1 + num2 + num3)/3)

Average()
calcAverage()



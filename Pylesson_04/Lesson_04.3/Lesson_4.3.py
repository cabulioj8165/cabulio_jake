num1 = 5
num2 = 7
sum = 0

def setNums():
    global num1, num2
    num1 = 8
    num2 = 13

def addNums():
    return num1 + num1

setNums()
print(addNums())

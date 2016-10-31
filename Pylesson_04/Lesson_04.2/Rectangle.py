length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

def calcPerim():
    global perim
    perim = 2*(length + width)
    return perim

def Print():
    print("your rectangle is {:.5f} feet around. ".format(perim))

calcPerim()
Print()

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perim = 0

def Perim():
    global perim, length, width
    perim = 2*(length + width)
def calcPerim():
    global perim
    print("The perimeter is {:.5f}".format(perim))
    perim = 2*(length + width)

def Print():
    print("your rectangle is {:.5f} feet around. ".format(perim))

Perim()
calcPerim()
Print()

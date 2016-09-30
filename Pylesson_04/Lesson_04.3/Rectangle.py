def Perim():
    global length, width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

def calcPerim():
    print("The perimeter of the rectangle is" , (2 * length) + (2 * width))

Perim()
calcPerim()

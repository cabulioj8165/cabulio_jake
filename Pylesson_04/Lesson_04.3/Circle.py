def Area():
    global radius
    radius = float(input("Enter the radius of the circle: "))

def calcArea():
    print("{}{:0.5f}".format("The area of the circle is " , 3.14 * radius**2))

Area()
calcArea()

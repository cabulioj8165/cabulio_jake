r = float(input("Enter the radius of the circle: "))
Area = 0

def Area():
    global Area, r
    Area = 3.1415 * r**2
def calcArea():
    global Area
    print("The area of the circle is {:.5f}".format(Area))
def Print():
    print("The area of a circle with a radius of" , r , "is {:.5f}".format(Area))

Area()
calcArea()
Print()

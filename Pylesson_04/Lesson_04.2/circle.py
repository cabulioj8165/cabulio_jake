r = float(input("Enter the radius of the circle: "))

def calcArea():
    global Area, r
    Area = 3.1415 * r**2
    return Area
def Print():
    print("The area of a circle with a radius of" , r , "is {:.5f}".format(Area))

calcArea()
Print()

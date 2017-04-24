length = float(input("Enter the length of the cube: "))
sa = 0

def SurfArea():
    global sa, length
    sa = length**2 * 6
def surfaceArea():
    global sa
    print("The surface area is {:.5f}".format(sa))

SurfArea()

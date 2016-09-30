def Surf():
    global side
    side = float(input("Enter the side of the cube: "))

def calcSurf():
    print("The surface area of the cube is" , 6 * (side**2))

Surf()
calcSurf()

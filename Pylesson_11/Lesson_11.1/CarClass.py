class Car:
    def __init__(self, p, i, e, t):
        self.p = p
        self.i = i
        self.e = e
        self.t = t

    def setCustom(self, p, i, e, t):
        self.p = p
        self.i = i
        self.e = e
        self.t = t

    def getPaint():
        return paintColor

    def getInterior():
        return interiorType

    def getEngine():
        return engineType

    def getTires():
        return tires

def main():
    p = input("Enter the color of your car: ")
    i = input("Enter the material in the interior: ")
    e = input("Enter the engine power: ")
    t = input("Enter the type of tires: ")

    newCar = Car(p, i, e, t)

    print("Your vehicle is ready...... \nPaint:" , p , "\nInterior:" , i , "\nEngine:" , e , "\nTires: " , t)

    print("\n")
    paint = input("ReEnter the color of your car: ")
    interior = input("ReEnter the material in the interior: ")
    engine = input("ReEnter the engine power: ")
    tires = input("ReEnter the type of tires: ")
    newCar.setCustom(p, i, e, t)
    print("Your vehicle is ready...... \nPaint:" , p , "\nInterior:" , i , "\nEngine:" , e , "\nTires: " , t)
    
main()

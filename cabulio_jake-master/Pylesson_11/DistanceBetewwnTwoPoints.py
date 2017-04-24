import math
class distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.distance = 0

    def newPoints(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.distance = 0

    def distanceCalc(self):
        self.distance = distance

    def getDistance(self):
        self.distance = math.sqrt((self.x2-self.x1)*(self.x2-self.x1)+(self.y2-self.y1)*(self.y2-self.y1))
        return self.distance

def main():
    x1 = float(input("Enter the first input: "))
    y1 = float(input("Enter the second input: "))
    x2 = float(input("Enter the third input: "))
    y2 = float(input("Enter the fourth input: "))

    dist = distance(x1, y1, x2, y2)

    print("distance = {:0.2f}".format(dist.getDistance()))

    print("\n")
    x1 = float(input("Reset the first input: "))
    y1 = float(input("Reset the second input: "))
    x2 = float(input("Reset the third input: "))
    y2 = float(input("Reset the fourth input: "))
    dist.newPoints(x1, y1, x2, y2)
    print("distance = {:0.2f}".format(dist.getDistance()))

main()

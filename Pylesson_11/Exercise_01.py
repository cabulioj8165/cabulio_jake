class MilesPerHour:
    def __init__(self, distance, hours, minutes):
        self.distance = distance
        self.hours = hours
        self.minutes = minutes
        self.mph = 0
        
    def setmph(self, distance, hours, minutes):
        self.distance = distance
        self.hours = hours
        self.minutes = minutes
        self.mph = 0   

    def distanceValue(self):
        return self.distance
    def getMph(self):
        self.mph = self.distance / (self.hours + self.minutes / 60)
        return self.mph
    def hoursValue(self):
        return self.hours
    def minutesValue(self):
        return self.minutes

def main():
    distance = int(input("Enter the distance: "))
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))

    mph = MilesPerHour(distance, hours, minutes)

    print(mph.distanceValue() , "Miles in" , mph.hoursValue() , "hours = {:0.2f}".format(mph.getMph()), "mph")
main()

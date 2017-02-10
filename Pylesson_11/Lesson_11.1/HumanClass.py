class Human:
    def __init__(self, hair, eyes, skin):
        self.hair = hair
        self.eyes = eyes
        self.skin = skin

    def setHES(self, hair, eyes, skin):
        self.hair = hair
        self.eyes = eyes
        self.skin = skin

    def getHair():
        return hairColor

    def getEyes():
        return EyeColor

    def getskin():
        return SkinInfo

def main():
    hair = input("Enter the color of your hair: ")
    eyes = input("Enter the color of your eyes: ")
    skin = input("Enter the color of your skin: ")

    newHuman = Human(hair, eyes, skin)

    print("Info:""\nHair:" , hair , "\nEyes:" , eyes , "\nSkin: " , skin)

    print("\n")
    hair = input("ReEnter the color of your hair: ")
    eyes = input("ReEnter the color of your eyes: ")
    skin = input("ReEnter the color of your skin: ")
    newHuman.setHES(hair, eyes, skin)
    print("Info:""\nHair:" , hair , "\nEyes:" , eyes , "\nSkin: " , skin)
    
main()

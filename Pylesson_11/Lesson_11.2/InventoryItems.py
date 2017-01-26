import random

class Item:
    def __init__(self, manu, name, categ = "", price = ""):
        self.manufacturer = manu
        self.name = name
        self.category = categ
        self.price = price
        self.UPC = random.randint(1000000000,9999999999)
    def __str__(self):
        return "Item Info:\nManufacturer: " + self.manufacturer + "\nName: " + self.name + "\nCategory: " + self.category + "\nPrice: " + self.price + "\nUPC: " + str(self.UPC)

def main():
    name = input("Enter the name of the item: ")
    manufacturer = input("Enter the manufacturer: ")
    
    ask = input("Will you enter the category and price information? (y or n): ")

    if ask == "y":
        category = input("Enter the category of the item(s): ")
        price = input("Enter the price of item(s): $")
        Item1 = Item(name, manufacturer, category, price)
    elif ask == "n":
        Item1 = Item(name, manufacturer)
        

    print(Item1.__str__())
    
main()

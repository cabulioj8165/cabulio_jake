import time
def format (item, price):
    print("* {:>10}  .........{:10.2f}".format(item, price))

def discount(subtotal):
    if subtotal > 2000:
        #print("Congragulations! You have a 15% discount! ")
        return subtotal * .15
    if subtotal <= 2000:
        #print("You only get a 15% discount if your total is over $2000.")
        return 0

item1 = input("Please enter item 1: ")
price1 = float(input("Please enter the price: "))
item2 = input("Please enter item 2: ")
price2 = float(input("Please enter the price:" ))
item3 = input("Please enter item 3: ")
price3 = float(input("Please enter the price: "))
item4 = input("Please enter item 4: ")
price4 = float(input("Please enter the price: "))
time.sleep(1)
subtotal = price1 + price2 + price3 + price4
tax = 0.08 * subtotal
discount = discount(subtotal)
total = subtotal + tax - discount

print("<<<<<<< Receipt >>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)
format("Subtotal: ", subtotal)
format("Tax: ", tax)
format("Discount: ", discount)
format("Total: ", total)

print("\n");

print("{:_>23}{:_>23}".format("", ""))
print("*Thank you for your support*")

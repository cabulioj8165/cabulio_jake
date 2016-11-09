import time
def format (item, price):
    print("* {:>10}  .........{:10.2f}".format(item, price))

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
discount = 0
def discount(discount, subtotal):
    if subtotal > 2000:
        print("Congragulations! You have a 15% discount! ")
        return discount == subtotal * .15
        print("* {:>10}  .........{:10.2f}".format("discount", discount))
    if subtotal <= 2000:
        print("You only get a 15% discount if your total is over $2000.")
        discount = 0
discount(discount, subtotal)
print("\n")
print("{:<>26}{:>>19}".format("__Receipt__", ""))
   
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)

print("\n");

if subtotal > 2000:
    print("* {:>10}  .........{:10.2f}".format("discount", subtotal * .15))
    format("subtotal: " , subtotal)

else:
    format("subtotal: " , subtotal)

tax = 0.08 * (price1 + price2 + price3 + price4)

format("tax: ", tax)

if subtotal > 2000:
    total = subtotal + tax - (subtotal * .15)
else:
    total = subtotal + tax

format("total: ", total)

print("{:_>23}{:_>23}".format("", ""))
print("*Thank you for your support*")

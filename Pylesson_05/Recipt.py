def format (item, price):
    print("* {:>10}  .........{:10.2f}".format(item, price))

#input item1
item1 = input("Please enter item 1: ")
price1 = float(input("Please enter the price: "))
#input item 2
item2 = input("Please enter item 2: ")
price2 = float(input("Please enter the price:" ))
#input item3
item3 = input("Please enter item 3: ")
price3 = float(input("Please enter the price: "))
item4 = input("Please enter item 4: ")
price4 = float(input("Please enter the price: "))

subtotal = price1 + price2 + price3 + price4
if subtotal > 2000:
    print("Congragulations! You have a 15% discount! ")
    
if subtotal < 2000:
    print("You only get a 15% discount if your total is over $2000.")
    

print("\n")
print("{:<>26}{:>>20}".format("__Recipt__", ""))
   
format(item1, price1)
format(item2, price2)
format(item3, price3)

print("\n");

format("subtotal: ", subtotal)

tax = 0.08 * (price1 + price2 + price3)

format("tax: ", tax)

total = subtotal + tax

format("total: ", total)

print("______________________________________________")

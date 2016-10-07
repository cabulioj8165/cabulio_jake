import time
def format (item, price):
    print("* {:>10}  .........{:10.2f}".format(item, price))

start = input("Welcome to McKing Burgers! Press enter for the menu. ")
print("* Burgers:                             * ")
time.sleep(.2)
print("* classic burger               $450.00 * ")
time.sleep(.2)
print("* veggie burger                $475.00 * ")
time.sleep(.2)
print("* bbq chicken burger           $520.00 * ")
time.sleep(.2)
print("* bacon double burger          $550.00 * ")
time.sleep(.2)
print("* Fries:                               * ")
time.sleep(.2)
print("* classic fries                $450.00 * ")
time.sleep(.2)
print("* cheese fries                 $485.00 * ")
time.sleep(.2)
print("* curly fries                  $500.00 * ")
time.sleep(.2)
print("* carne asada fries            $525.00 * ")
time.sleep(.2)
print("* Beverages:                           * ")
time.sleep(.2)
print("* (sm, med, lrg)drink $420, $435, $475 * ")
time.sleep(.2)
print("* beer                         $485.00 * ")
time.sleep(.2)
print("* snapple                      $475.00 * ")
time.sleep(.2)
print("* Shakes/ Ice Cream:           $450.00 * ")
time.sleep(.2)
print("* malt                         $460.00 * ")
time.sleep(.2)
print("* shake                        $460.00 * ")
time.sleep(.2)
print("* ice cream cone               $470.00 * ")
time.sleep(.2)
print("* ice cream sundae             $480.00 * ")
time.sleep(.2)
print("\n")
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
discount = (price1 + price2 + price3 + price4) * .15
if subtotal > 2000:
    print("Congragulations! You have a 15% discount! ")

if subtotal <= 2000:
    print("You only get a 15% discount if your total is over $2000.")

print("\n")
print("{:<>26}{:>>20}".format("__Recipt__", ""))
   
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)

print("\n");

if subtotal > 2000:
    format("discount: " , discount)
    format("subtotal: " , subtotal)
    
else:
    format("subtotal: " , subtotal)

tax = 0.08 * (price1 + price2 + price3)

format("tax: ", tax)

if subtotal > 2000:
    total = discount + subtotal + tax
else:
    total = subtotal + tax

format("total: ", total)

print("{:_>23}{:_>23}".format("", ""))

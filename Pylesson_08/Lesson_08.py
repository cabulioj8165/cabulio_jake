number = int(input("Please enter a number: "))

def recur(number):
   if(number == 0):
       return 1
   else:
       return number * recur(number - 1)

print(recur(number))

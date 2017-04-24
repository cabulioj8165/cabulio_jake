number = int(input("What do you want the interger to be? "))
x = int(input("Enter the size of the table: "))

def table():
    for i in range(1, x + 1):
        print(i * number)   
table()

def format(height, length, width):

    V = (length*width*height)/1728
    return("{:0.2f}".format(V))
    

x = input("This is a program to calculate cubic inches to cubic feet of a box. Press enter. ")
height = float(input("Please enter the height of the box in inches: "))
length = float(input("Please enter the length of the box in inches: "))
width = float(input("Please enter the width of the box in inches: "))

print("The box is" , format(height, length, width) , "Cubic feet.")


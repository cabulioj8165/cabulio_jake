def format(r, P, n, t):
    
    A = P*(1+(r/n))**(n*t)
    return("{:0.2f}".format(A))
    
rate = float(input("Please enter the interest rate: "))
Principle = float(input("Please enter the principal: "))
number = float(input("Please enter the number of times the loan is compunded per year: "))
time = float(input("Please enter the life of the loan(in years): "))
months = time/12

print("The total amount of the loan is" , format(rate, Principle, number, months
                                                 ))

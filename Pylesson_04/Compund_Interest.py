def format(r, P, n, t):
    
    A = P*(1+(r/n))**(n*t)
    print("{:10.2f}".format(A))
    

r = float(input("Please enter the interest rate: "))
P = float(input("Please enter the principal: "))
n = float(input("Please enter the number of times the loan is compunded per year: "))
t = float(input("Please enter the life of the loan(in years): "))

format(r, P, n, t)

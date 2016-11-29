expression = input("Please enter a mathmatical expression: ")
equation = expression.split()
i = 0
while i < len(equation):
    if i < len(equation) and equation[i] == "*" or "/":
        if equation[i] == "*":
            equation[i] == (equation[i - 1]) * (i + 1)
        else:
            equation[i] == (equation[i - 1]) / (i + 1)
        equation.remove(equation[i - 1])
        equation.remove(equation[i])
    i = i + 1
while i < len(equation):
    if i < len(equation) and equation[i] == "+" or "-":
        if equation[i] == "+":
            equation[i] == (equation[i - 1]) + (i + 1)
        else:
            equation[i] = (equation[i - 1]) - (i + 1)
        equation.remove(equation[i - 1])
        equation.remove(equation[i])
    i = i + 1
print(equation)


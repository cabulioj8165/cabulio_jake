start = input("This is a GPA calculator. press enter to continue. ")
math = input("Enter the letter grade that you have in math: ")
science = input("What science do you take? ")
science1 = input("Enter the letter grade that you have in " + science + ": ")
pe = input("Enter the letter grade that you have in your PE class: ")
language = input("What language are you taking? ")
language1 = input("Enter the letter grade that you have in " + language + ": ")
english = input("Enter the letter grade that you have in english: ")
elective1a = input("What elective do you take? ")
elective1b = input("Enter the grade that you have in " + elective1a + ": ")
elective2a = input("What is the other elective that you take? ")
elective2b = input("Enter the grade that you have in " + elective2a + ": ")

def calcPoints(Math):
    if math == "a" or "A":
        return 4.0
    elif math == "b" or "B":
        return 3.0
    elif math == "c" or "C":
        return 2.0
    elif math == "d" or "D":
        return 1.0
    else:
        return 0
    if science1 == "a" or "A":
        return 4.0
    elif science1 == "b" or "B":
        return 3.0
    elif science1 == "c" or "C":
        return 2.0
    elif science1 == "d" or "D":
        return 1.0
    else:
        return 0
    if language1 == "a" or "A":
        return 4.0
    elif language1 == "b" or "B":
        return 3.0
    elif language1 == "c" or "C":
        return 2.0
    elif language1 == "d" or "D":
        return 1.0
    else:
        return 0
    if english == "a" or "A":
        return 4.0
    elif english == "b" or "B":
        return 3.0
    elif english == "c" or "C":
        return 2.0
    elif english == "d" or "D":
        return 1.0
    else:
        return 0
    if elective1b == "a" or "A":
        return 4.0
    elif elective1b == "b" or "B":
        return 3.0
    elif elective1b == "c" or "C":
        return 2.0
    elif elective1b == "d" or "D":
        return 1.0
    else:
        return 0
    if elective2b == "a" or "A":
        return 4.0
    elif elective2b == "b" or "B":
        return 3.0
    elif elective2b == "c" or "C":
        return 2.0
    elif elective2b == "d" or "D":
        return 1.0
    else:
        return 0

GPA = float((calcPoints(

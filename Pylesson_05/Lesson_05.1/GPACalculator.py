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

def calcPoints(grade):
    if grade == "a":
        return 4.0
    elif grade == "b":
        return 3.0
    elif grade == "c":
        return 2.0
    elif grade == "d":
        return 1.0
    else:
        return 0

GPA = (calcPoints(math) + calcPoints(science1) +calcPoints(pe) +calcPoints(language1) +calcPoints(elective2b) +calcPoints(english) +calcPoints(elective1b)) / 7

if GPA == 4:
    print("Your GPA is " , GPA , ". That is really good! ")
elif GPA > 3:
    print("Your GPA is " , GPA , ". That is not bad. ")
elif GPA > 2:
    print("Your GPA is " , GPA , ". You need to study more. ")
elif GPA > 1:
    print("Your GPA is " , GPA , ". You need a lot mroe studying. ")

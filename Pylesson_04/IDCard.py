name1 = input("Enter your first name: ")
name2 = input("Enter your last name: ")
title = input("Enter your title: ")
school = input("Enter the school site: ")
year = input("Enter the school year: ")
subject = input("What is your subject: ")

def printf(name, lname, title, school, year, subject):
    print("\n")
    print("\n")
    print("{:*>16}{:*>16}".format("*", ""))
    print("*{:>12}{:>17} *".format(school, year))
    print("*{:>12}{:>17} *".format(name, lname))
    print("*{:>12}{:>17} *".format(title, subject))
    print("{:*>16}{:*>16}".format("*", ""))

printf(name1, name2, title, school, year, subject)

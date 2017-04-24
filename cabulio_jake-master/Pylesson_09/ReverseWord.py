myList = ["hi", "bye", "idk", "apple", "pie"]

print("In order...")
for i in range(0, len(myList)):
        print(myList[i])
print("\n")
print("Reversed...")
def reverse():
        for i in range(len(myList)-1, -1, -1):
                print(myList[i])
reverse()

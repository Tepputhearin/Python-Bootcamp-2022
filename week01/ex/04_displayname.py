user = input("Enter your name:")
num = int(input("Enter number of times to display:"))
if user == "":
    print("No name entered")
else:
    for i in range(0, num):
        print(user)
user = input("Input a string:")
if user == "":
    print("The string is empty")
else:
    for i in user:
        print(f"{i}:{ord(i)}")
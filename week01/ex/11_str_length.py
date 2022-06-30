def string():
    user = input("Enter a string:\n")
    if user == "":
        print("The string is empty")
    else:
        l = len(user)
        print(l)
string()
def string():
    user = input("Input a string:")
    if user == "":
        print("The string is empty")
    else:
        print(user.lower())
string()
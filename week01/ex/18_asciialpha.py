def string():
    user = input("Input a text:")
    if user == "":
        print("The string is empty")
    else:
        for i in user:
            print(f"{i}:{ord(i)}")
string()
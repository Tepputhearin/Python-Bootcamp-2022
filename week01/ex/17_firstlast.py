def string():
    user = input("Input a string:")
    if user == "":
        print("The string is empty")
    else:
        l = len(user)-1
        after = user[l]
        before = user[0]
        print(f"First Character:{before}")
        print(f"Last Character:{after}")

string()
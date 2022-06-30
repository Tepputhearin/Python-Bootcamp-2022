def string():
    user = input("Input a text:")
    if user == "":
        print("The string is empty")
    else:
        l = len(user)
        mid = l // 2
        after = user[mid:]
        before = user[:mid]
        print(before)
        print(after)

string()
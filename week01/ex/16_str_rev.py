def string():
    user = input("Input a string:")
    if user == "":
        print("The string is empty")
    else:
        l = len(user)
        mid = l // 2
        after = user[mid:]
        before = user[:mid]
        before_re = before[::-1]
        print(before_re + after)
string()
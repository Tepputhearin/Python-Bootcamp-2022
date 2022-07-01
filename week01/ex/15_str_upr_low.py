user = input("Enter a string:")
if user == "":
    print("The string is empty")
else:
    l = len(user)
    mid = l // 2
    after = user[mid:]
    before = user[:mid]
    print(before.upper()+after.lower())
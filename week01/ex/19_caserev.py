user = input("Enter a string:")
list = []
if user == "":
    print("Empty")
else:
    for i in user:
        if i.isupper():
            l = i.lower()
            list.append(l)
        else:
            u = i.upper()
            list.append(u)
print("".join(list))
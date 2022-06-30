list = []
while True:
        user = input("Input number:")
        if user == "stop":
            break
        elif user.isdecimal():
            list.append(int(user))
        else:
            print("Not valid")
result = sum(list)
print(f"The Sum is:{result}")
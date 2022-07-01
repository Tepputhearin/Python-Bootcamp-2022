list = []
while True:
        user = input("Input a number:")
        if user == "stop":
            break
        elif user.isdecimal():
            list.append(int(user))
        else:
            print("This input must be a valid number")
result = sum(list)
print(f"The Sum is:{result}")
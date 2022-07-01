user_num = input("Input a number:\n")
if user_num.isdecimal():
    if int(user_num) % 2 == 0:
            print("Even Number")
    else:
            print("Odd Number")
else:
    print("Not a valid Number")
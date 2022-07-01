try:
    user_num = int(input("Input a number:\n"))
    if user_num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
except ValueError:
    print("Not a valid Number")
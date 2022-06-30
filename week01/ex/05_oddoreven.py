try:
    user_num = int(input("Input a number:\n"))
    if user_num % 2 == 0:
        print("The number you have entered is Even")
    else:
        print("The number you have entered is Odd")
except ValueError:
    print("Not a valid Number")
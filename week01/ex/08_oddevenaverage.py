num = 0
oddSum = []
evenSum = []
user = input("Input a number:")
if user.isdecimal():
    num = int(user)
    for i in range(num + 1):
        if i % 2 == 0:
            evenSum.append(i)
        else:
            oddSum.append(i)
    print(f"Average of odd numbers = {sum(oddSum) / len(oddSum)}")
    print(f"Average of even numbers = {sum(evenSum) / len(evenSum)}")
else:
    print("Invalid input")

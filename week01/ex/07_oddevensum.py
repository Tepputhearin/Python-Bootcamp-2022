num = 0
oddSum = []
evenSum = []
try:
    num = int(input("Input a number:"))
except ValueError:
    print("Invalid input")
for i in range(num+1):
    if i%2 == 0:
        evenSum.append(i)
    else:
        oddSum.append(i)
print(f"Sum of odd numbers = {sum(oddSum)}")
print(f"Sum of even numbers = {sum(evenSum)}")
num = 0
oddSum = []
evenSum = []
try:
    user = int(input("input:"))
    num = user
except ValueError:
    print("invalid input")
for i in range(num+1):
    if i%2 == 0:
        evenSum.append(i)
    else:
        oddSum.append(i)
print(f"Sum of odd numbers = {sum(oddSum)}")
print(f"Sum of even numbers = {sum(evenSum)}")
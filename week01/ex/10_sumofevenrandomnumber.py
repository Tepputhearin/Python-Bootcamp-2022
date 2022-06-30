user = int(input("Input Number:"))
import random
list = []
while len(list) < user:
    a = random.randint(2000,3000)
    if a%2 == 0:
        add = list.append(a)
        print(list)
print(f"Sum of even random numbers:{sum(list)}")
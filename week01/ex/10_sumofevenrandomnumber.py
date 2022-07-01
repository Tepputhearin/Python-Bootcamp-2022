user = int(input("Input Number:"))
import random
list = []
for i in range(0,user):
    a = random.randint(2000,3000)
    if a%2 == 0:
        add = list.append(a)
print(f"Sum of even random numbers:{sum(list)}")
def random_tuple(num):
    list = []
    import random
    for i in range(num):
        ran = random.randint(0,100)
        print(f"Random number {i+1} : {ran}")
        list.append(ran)
    tup = tuple(list)
    print(tup)
    return sum(list)
print(random_tuple(5))
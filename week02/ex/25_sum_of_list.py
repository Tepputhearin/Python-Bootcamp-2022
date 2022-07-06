def Sum_of_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(Sum_of_list([20,15,10,30]))
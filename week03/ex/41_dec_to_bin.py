def dec_to_bin(num):
    num = str(num)
    new_num = []
    reverse = []
    i = 0
    while num != 0:
        num_int = int(num)
        new = num_int % 2
        num = num_int//2
        new_num.append(str(new))
        i += 1
    for j in range(i-1,-1,-1):
        reverse.append(new_num[j])
        print(reverse)
    print("".join(reverse))
    return


dec_to_bin(50)

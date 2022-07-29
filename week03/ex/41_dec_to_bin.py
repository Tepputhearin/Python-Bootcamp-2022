def dec_to_bin(num):
    bin = []
    while num != 0:
        bin_num = num % 2
        num = int(num / 2)
        bin.append(bin_num)
    for j in range(len(bin) - 1, -1, -1):
        print(bin[j], end="")
    return


dec_to_bin(50)

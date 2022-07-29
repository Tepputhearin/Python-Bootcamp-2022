def dec_to_oct(num):
    oct = []
    while num != 0:
        octal_num = num % 8
        num = int(num/8)
        oct.append(octal_num)
    for j in range(len(oct) - 1, -1, -1):
        print(oct[j], end="")
    return

dec_to_oct(98)
def bin_to_dec(num):
    num = str(num)
    b = {'0','1'}
    t = set(num)
    if b == t or t =={'0'} or t== {'1'}:
        num = int(num)
        decimal = 0
        i = 0
        while num != 0:
            dec = num % 10
            decimal = decimal + dec * pow(2, i)
            num = num // 10
            i += 1
        print(decimal)
    else:
        print("This is not a binary number")
    return


bin_to_dec(110011)
def bin_to_hex(num):
    table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
             13: 'D', 14: 'E', 15: 'F'}
    num = str(num)
    hexa = ''
    b = {'0', '1'}
    t = set(num)
    if b == t or t == {'0'} or t == {'1'}:
        num = int(num)
        decimal = 0
        i = 0
        while num != 0:
            dec = num % 10
            decimal = decimal + dec * pow(2, i)
            num = num // 10
            i += 1
        while decimal > 0:
            remain = decimal % 16
            hexa = table[remain] + hexa
            decimal = decimal // 16
        print(hexa)
        return
    else:
        print("This is not a binary number")

bin_to_hex(11001101)
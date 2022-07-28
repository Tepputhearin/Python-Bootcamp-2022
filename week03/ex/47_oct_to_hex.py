def oct_to_hex(oct):
    table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
             13: 'D', 14: 'E', 15: 'F'}
    octa = str(oct)
    decimal = []
    deci = 0
    new_deci = []
    l = 0
    hexa = ''
    for i in range(len(octa)):
        decimal.append(octa[i])
    for j in range(len(octa)-1,-1,-1):
        power = pow(8, j)
        decim = int(decimal[l])*(power)
        new_deci.append(decim)
        deci += int(decimal[l])
        l += 1

    full = sum(new_deci)
    if deci % 7 == 0:
        print("This is not an octal number")
    else:
        while full > 0:
            remain = full % 16
            hexa = table[remain] + hexa
            full = full // 16
        print(hexa)
    return

oct_to_hex(1271)
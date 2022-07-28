def oct_to_dec(num):
    octa = str(num)
    decimal = []
    deci = 0
    new_deci = []
    l = 0
    for i in range(len(octa)):
        decimal.append(octa[i])
    for j in range(len(octa)-1,-1,-1):
        power = pow(8, j)
        decim = int(decimal[l])*(power)
        new_deci.append(decim)
        deci += int(decimal[l])
        l += 1
    if deci % 7 ==0:
        print(sum(new_deci))
        print("This is not an octal number")
    else:
        print(sum(new_deci))
    return

oct_to_dec(750)
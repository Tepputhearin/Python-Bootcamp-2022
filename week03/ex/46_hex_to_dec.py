def hex_to_dec(hex):
    table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    y = 0
    ind = []
    new_ind = []
    keys = table.keys()
    for i in hex:
        ind.append(i)
    for s in range(len(ind)):
        if ind[s] not in keys:
            print("This is not a hexa-decimal number")
            return
    else:
        for j in range(len(ind) - 1, -1, -1):
            power = pow(16, j)
            deci = table[ind[y]]*power
            new_ind.append(deci)
            y += 1
        print(sum(new_ind))
    return

hex_to_dec("BA1")
def xor_operation(hex1,hex2):
    result = []
    result1 = bin(int(hex1,16))
    result2 = bin(int(hex2,16))
    new_result1 = result1[2:]
    new_result2 = result2[2:]
    for i in range(len(new_result1)):
        new_result3 = int(new_result1[i:i+1]) ^ int(new_result2[i:i+1])
        result.append(str(new_result3))
    print(f"{new_result1}\n{new_result2}\n")
    print("".join(result))
    return
xor_operation("33","3D")
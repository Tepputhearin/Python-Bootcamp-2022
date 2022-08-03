def or_operation(hex1,hex2):
    result = ""
    result1 = bin(int(hex1,16))
    result2 = bin(int(hex2,16))
    new_result1 = result1[2:]
    new_result2 = result2[2:]
    for i in range(len(new_result1)):
        if new_result1[i:i+1] == "1" or new_result2[i:i+1] == "1":
            result = result + "1"
        else:
            result = result + "0"
    print(f"{new_result1}\n{new_result2}\n")
    print(result)
    return
or_operation("33","3D")
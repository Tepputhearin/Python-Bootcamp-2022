def binary_subtraction(num1,num2):
    num3 = num1 - num2
    carry = 0
    result = ""
    num1 = bin(num1)[2:]
    num2 = bin(num2)[2:]
    max_len = max(len(num1),len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    for i in range(len(num1) - 1, -1, -1):
        num = int(num1[i]) - int(num2[i]) - carry
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        if num < 0:
            carry = 1
        else:
            carry = 0
    if carry != 0:
        result += "01"
    print(f"Num1                   :{num1}\nNum2                   :{num2}")
    print(f"Difference(Binary)     :{result[::-1]}\nDifference(Decimal)    :{num3}")
    return


binary_subtraction(60,50)

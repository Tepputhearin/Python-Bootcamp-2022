def binary_addition(num1,num2):
    num3 = num1 + num2
    carry = 0
    result = ""
    num1 = bin(num1)[2:]
    num2 = bin(num2)[2:]
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    for i in range(len(num1)-1,-1,-1):
        num = str(int(num1[i]) + int(num2[i]) + carry)
        carry = 0
        if num == "2":
            carry = 1
            result += "0"
        elif num == "3":
            carry = 1
            result += "1"
        else:
            result += num
    if carry != 0:
        result += "1"
    print(f"Num1            :{num1}\nNum2            :{num2}")
    print(f"Sum(Binary)     :{result[::-1]}\nSum(Decimal)    :{num3}")
    return

binary_addition(60,50)
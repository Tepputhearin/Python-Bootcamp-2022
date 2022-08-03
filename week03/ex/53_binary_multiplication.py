def binary_multiplication(num1,num2):
    num4 = num1 * num2
    carry = 0
    l = 0
    list = []
    result = ""
    result1 = ""
    num1 = bin(num1)[2:]
    num2 = bin(num2)[2:]
    for j in range(len(num2)-1,-1,-1):
        result = ""
        mul = int(num1) * int(num2[j])
        for i in range(len(num1) - 1, -1, -1):
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
    print(f"Num1                :{num1}\nNum2                :{num2}")
    print(f"Product(Binary)     :{result[::-1]}\nProduct(Decimal)    :{num4}")
    return


binary_multiplication(60,50)
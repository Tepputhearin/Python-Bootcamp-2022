def binary_multiplication(num1, num2):       # Do manual on spare time almost done though
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    bin3 = bin(int(bin1,2)*int(bin2,2))[2:]
    num3 = num1*num2
    print(f"Num1                :{bin1}\nNum2                :{bin2}")
    print(f"Product(Binary)     :{bin3}\nProduct(Decimal)    :{num3}")


binary_multiplication(60,50)
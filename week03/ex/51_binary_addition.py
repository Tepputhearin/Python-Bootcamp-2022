def binary_addition(num1,num2):
    Num1 = []
    Num2 = []
    Num3 = []
    new_Num1 = []
    new_Num2 = []
    new_Num3 =[]
    sum = num1 + num2
    dict = {"Num1": Num1, "Num2": Num2, "new_Num1": new_Num1, "new_Num2": new_Num2, "Num3": Num3, "new_Num3": new_Num3}
    Nums = [num1, num2, sum]
    l = 0
    for i in Nums:
        j, p = "Num"+f"{1+l}", "new_Num"+f"{1+l}"
        j = dict[j]
        l += 1
        while i != 0:
            bin_num = int(i % 2)
            i = int(i / 2)
            j.append(str(bin_num))
        for d in range(len(j) - 1, -1, -1):
            dict[p].append(j[d])
    print("Num1         :"+"".join(new_Num1))
    print("Num2         :"+"".join(new_Num2))
    print("Sum(Binary)  :"+"".join(new_Num3))
    print("Sum(Decimal) :"+str(sum))
    return

binary_addition(60,50)
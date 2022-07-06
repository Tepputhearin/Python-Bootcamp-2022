def fun_calc(num1,num2, operator):
        if operator == "+":
            result = int(num1) + int(num2)
            print(result)
        elif operator == "-":
            result = int(num1) - int(num2)
            print(result)
        elif operator == "*":
            result = int(num1) * int(num2)
            print(result)
        elif operator == "/":
            result = int(num1) / int(num2)
            print(result)
        return f"Process :{num1}{operator}{num2} = {result}"
print(fun_calc(50,2,'*'))
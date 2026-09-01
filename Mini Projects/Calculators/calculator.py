#Calculator

operator = input("Enter an operator (+, -, *, /)")

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if operator == "+":
    result = num1+num2
    print(round(result, 3))
elif operator == "-":
    result = num1-num2
    print(round(result, 3))
elif operator == "*":
    result = num1*num2
    print(round(result, 3))
elif operator == "/":
    result = num1/num2
    print(round(result, 3))
else:
    print(f"{operator} is NOT a valid operator")
# python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(num1, operator, num2)
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
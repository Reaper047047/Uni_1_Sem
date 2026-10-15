import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
symbol = input("Enter the symbol: ")

if symbol == "+":
    print(num1 + num2)
elif symbol == "-":
    print(num1 - num2)
elif symbol == "*":
    print(num1 * num2)
elif symbol == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1 / num2)
else:
    print("Error: Invalid symbol. Please use +, -, *, or /.")
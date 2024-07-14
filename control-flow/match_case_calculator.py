#!/usr/bin/python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
#resultplus = num1 + num2
#resultminus = num1 - num2
#resulttimes = num1 * num2
#resultdiv = num1 / num2
if operation == "+":
    print(f"the result is {num1 + num2}.")
elif operation == "*":
    print(f"the result is {num1 * num2}.")
elif operation == "-":
    print(f"the result is {num1 - num2}.")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"the result is {num1 / num2}.")

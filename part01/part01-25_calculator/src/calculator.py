# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
print(f"\n")
if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
if operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")
if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
# Write your solution here
days = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
grocery_money = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {(grocery_money/7) + ((price * days) / 7)} euros")
print(f"Weekly: {grocery_money + (price * days)} euros")
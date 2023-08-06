# Write your solution here
temp = int(input("Please type in a temperature (F): "))
celsius = (temp - 32) * (5/9)
print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print(f"Brr! It's cold in here!")
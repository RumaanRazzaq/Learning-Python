# Write your solution here
age = int(input("What is your age? "))
if age > 4:
    print(f"Ok, you're {age} years old")
elif age > -1:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
# Write your solution here
number = int(input("Please type in a number: "))
i = 1
while i <= number:
    if number - 1 >= i:
        print(str(i+1))
        print(str(i))
    i += 2
if number % 2 != 0:
    print(str(i-2))
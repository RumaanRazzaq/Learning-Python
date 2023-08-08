# Write your solution here
number = int(input("Please type in a positive integer: "))
for i in range(number * -1, number + 1):
    if i != 0:
        print(i)
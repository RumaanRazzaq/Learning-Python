# Write your solution here
sum = 1
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    count = 1
    while count <= number:
        sum *= count
        count += 1
    print(f"The factorial of the number {number} is {sum}")
    sum = 1
print("Thanks and bye!")
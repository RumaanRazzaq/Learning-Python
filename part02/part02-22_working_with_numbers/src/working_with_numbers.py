# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
positive_num = 0
negative_num = 0

while True:
    number = int(input("Number: "))
    count += 1
    sum += number
    if number == 0:
        break
    elif number > 0:
        positive_num += 1
    else:
        negative_num += 1

print(f"Numbers typed in {count - 1}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / (count - 1)}")
print(f"Positive numbers {positive_num}")
print(f"Negative numbers {negative_num}")
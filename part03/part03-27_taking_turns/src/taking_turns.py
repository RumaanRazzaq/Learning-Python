# Write your solution here
number = int(input("Please type in a number: "))
temp_num = number
i = 1
while i < number:
    print(str(i))
    print(str(number))
    i += 1
    number -= 1

if temp_num % 2 != 0:
    print(str(i))
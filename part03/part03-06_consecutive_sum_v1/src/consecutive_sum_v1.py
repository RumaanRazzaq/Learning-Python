# Write your solution here
number = int(input("Limit: "))
sum = 0
count = 1
while sum < number:
    sum += count
    count += 1
print(f"{sum}")
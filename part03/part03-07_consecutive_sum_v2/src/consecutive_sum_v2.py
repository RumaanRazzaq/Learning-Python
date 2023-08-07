# Write your solution here
number = int(input("Limit: "))
sentance = "The consecutive sum: "
sum = 0
count = 1
while sum < number:
    if(sum + count < number):
        sentance += f"{count} + "
    else:
        sentance += f"{count} "
    sum += count
    count += 1
sentance += f"= {sum}"
print(f"{sentance}")
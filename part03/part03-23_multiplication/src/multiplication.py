# Write your solution here
number = int(input("Please type in a number: "))
sentence = ""
count1 = 1
count2 = 1
while True:
    if count1 > number:
        break
    while count1 <= number:
        if count2 > number:
            break
        sentence = f"{count1} x {count2} = {count1 * count2}"
        print(sentence)
        count2 += 1
    count1 += 1
    count2 = 1
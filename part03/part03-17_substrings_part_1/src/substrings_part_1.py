# Write your solution here
count = 1
word = input("Please type in a string: ")
while count != len(word) + 1:
    print(word[:count])
    count += 1
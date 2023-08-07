# Write your solution here
word = input("Please type in a string: ")
count = len(word) - 1
while count != -1:
    print(word[count:])
    count -= 1
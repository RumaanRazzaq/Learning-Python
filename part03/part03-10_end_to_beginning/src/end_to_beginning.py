# Write your solution here
word = input("Please type in a string: ")
index = len(word) - 1
while index > -1:
    print(f"{word[index]}")
    index -= 1
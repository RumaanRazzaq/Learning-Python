# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
i = 0
while i < len(word) - 2:
    if word[i] == character:
        print(word[i:i+3])
    i += 1
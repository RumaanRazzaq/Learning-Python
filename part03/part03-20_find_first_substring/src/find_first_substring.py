# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
if index != -1 and len(word) - 4 >= index:        
    print(word[index] + word[index + 1] + word[index + 2])
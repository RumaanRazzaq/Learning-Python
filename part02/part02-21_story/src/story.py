# Write your solution here
story = ""
tempWord = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or tempWord == word:
        break
    tempWord = word
    story += word + " "
print(story)

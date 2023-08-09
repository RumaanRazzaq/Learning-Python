# Write your solution here
from difflib import get_close_matches

text = input("write text: ")
list = []
with open("src/wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        list.append(line)
words = text.split(" ")
suggestions = {}
for word in words:
    if word.lower() not in list:
        suggestions[word] = get_close_matches(word, list)
        word = "*" + word + "*"
    print(word + " ", end = "")

print("\nsuggestions:")
for suggestion in suggestions:
    print(suggestion + ": ", end="")
    for word in suggestions[suggestion]:
        print(word + ", ", end="")
    print()
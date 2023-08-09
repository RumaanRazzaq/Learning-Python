# write your solution here
text = input("Write text: ")
list = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        list.append(line)
words = text.split(" ")
for word in words:
    if word.lower() not in list:
        word = "*" + word + "*"
    print(word + " ", end = "")
# Write your solution here
word = input("Word: ")
start = (28 - len(word)) // 2
print("*" * 30)
if(len(word) % 2 == 0):
    end = start
else:
    end = start + 1

print("*" + " " * start + word + " " * end + "*")
print("*" * 30)
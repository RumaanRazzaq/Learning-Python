# Write your solution here
list = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index:"))
    if index == -1:
        break
    val = int(input("New value:"))
    if index >= len(list):
        continue
    list[index] = val
    print(list)
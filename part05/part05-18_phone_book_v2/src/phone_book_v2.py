# Write your solution here
def search(phonebook):
    name = input("name: ")
    if name not in phonebook:
        print("no number")
    else:
        for num in phonebook[name]:
            print(num)

def add(phonebook):
    name = input("name: ")
    number = input("number: ")

    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(number)

    print("ok!")

def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            search(phonebook)
        if command == 2:
            add(phonebook)
        if command == 3:
            break
    print("quitting...")

main()

# 2
# mary
# 040-234567
# 1
# mary
# 3
# expected print out is
# ok!
# 040-234567 09-334455
# quitting...
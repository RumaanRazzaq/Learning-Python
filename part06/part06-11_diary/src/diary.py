# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    elif function == 1:
        with open("diary.txt", "a") as file:
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            print("Diary saved")
    elif function == 2:
        with open("diary.txt") as file:
            for line in file:
                print(line)
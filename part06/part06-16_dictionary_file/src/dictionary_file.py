# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        data = f"{finnish_word} {english_word}"
        with open("src/dictionary.txt", "a") as file:
            file.write(data + "\n")
        print("Dictionary entry added")
    elif function == 2:
        dictionary = {}
        search = input("Search term: ")
        with open("src/dictionary.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                words = line.split(" ")
                dictionary[words[0]] = words[1]
        output = []
        for key, val in dictionary.items():
            if search in key:
                output.append((key, val))
            elif search in val:
                output.append((key, val))
        for items in output:
            sentence = items[0] + " - " + items[1]
            print(sentence)
    elif function == 3:
        print("Bye!")
        break
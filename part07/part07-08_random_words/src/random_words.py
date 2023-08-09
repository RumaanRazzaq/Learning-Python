# Write your solution here
import string
from random import shuffle, sample

def comparison(word, search_term):
    if len(search_term) > len(word):
        return False
    for i in range(0, len(search_term)):
        if search_term[i] != word[i]:
            return False
    return True

def words(n: int, beginning: str):
    list = []
    with open("src/words.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            list.append(line)

    word_list = []
    count = 0
    for word in list:
        if comparison(word, beginning) == True:
            word_list.append(word)
            count += 1
    
    shuffle(word_list)

    return sample(word_list, n)

if __name__ == "__main__":
    print(len(words(10, "a")))
    print(comparison("trueman", "true"))

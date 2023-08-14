# Write your solution here:
from random import randint

def word_generator(characters: str, length: int, amount: int):
    count = 0
    while count < amount:
        string = ""
        for i in range(0, length):
            string += characters[randint(0, len(characters) - 1)]
        yield string
        count += 1
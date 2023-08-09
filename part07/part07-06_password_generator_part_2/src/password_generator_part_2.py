# Write your solution here
from random import *
import string

def generate_strong_password(amount: int, number: bool, special: bool):
    lowercase = list(string.ascii_lowercase)
    special_char = ["!", "?", "=", "+", "-", "(", ")", "#"]
    shuffle(special_char)
    shuffle(lowercase)
    password = ""
    for i in range(0, amount):
        if number == True:
            password += str(randint(0, 9))
            number = False
            continue
        elif special == True:
            password += special_char[randint(0, 7)]
            special = False
            continue
        password += lowercase[i]
    return password

if __name__ == "__main__":
    print(generate_strong_password(8, True, True))
# Write your solution here
from random import *
import string

def generate_password(amount: int):
    lowercase = list(string.ascii_lowercase)
    shuffle(lowercase)
    password = ""
    for i in range(0, amount):
        password += lowercase[i]
    return password
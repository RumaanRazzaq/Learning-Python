# Write your solution here
from string import ascii_lowercase, ascii_uppercase, digits

def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char in ascii_uppercase:
            new_string += char.lower()
        elif char in ascii_lowercase:
            new_string += char.upper()
        else:
            new_string += char
    return new_string

def split_in_half(orig_string: str):
    midpoint = len(orig_string) // 2
    first = orig_string[:midpoint]
    last = orig_string[midpoint:]
    return (first, last)

def remove_special_characters(orig_string: str):
    new_string = ""
    for character in orig_string:
        if character == ' ' or character in ascii_lowercase or character in ascii_uppercase or character in digits:
            new_string += character
    return new_string
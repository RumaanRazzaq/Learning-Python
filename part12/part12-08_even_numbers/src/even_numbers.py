# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning
    if number % 2 != 0:
        number += 1
    if maximum % 2 != 0:
        maximum -= 1
    while number <= maximum:
        yield number
        number += 2
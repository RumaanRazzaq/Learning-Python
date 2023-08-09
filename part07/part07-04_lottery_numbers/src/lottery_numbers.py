# Write your solution here
from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper + 1))
    draw = sample(number_pool, amount)
    draw.sort()
    return draw

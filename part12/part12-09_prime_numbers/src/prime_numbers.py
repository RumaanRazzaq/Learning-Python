# Write your solution here
def prime_numbers():
    number = 2
    while True:
        for a in range(2,number):
            if number % a ==0:
                break
        else:
            yield number
        number += 1
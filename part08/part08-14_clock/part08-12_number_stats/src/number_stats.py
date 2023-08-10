# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.list = []

    def add_number(self, number:int):
        self.numbers += 1
        self.list.append(number)

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers == 0:
            return 0
        return sum(self.list)
    
    def average(self):
        if self.numbers == 0:
            return 0
        return sum(self.list) / self.count_numbers()
    
print("Please type in integer numbers:")
all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:
    number = int(input())
    if number == -1:
        break
    elif number % 2 == 0:
        even_stats.add_number(number)
    elif number % 2 != 0:
        odd_stats.add_number(number)
    all_stats.add_number(number)

print(f"Sum of numbers: {all_stats.get_sum()}")
print(f"Mean of numbers: {all_stats.average()}")
print(f"Sum of even numbers: {even_stats.get_sum()}")
print(f"Sum of odd numbers: {odd_stats.get_sum()}")
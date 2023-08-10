# Write your solution here
class Checklist:
    def __init__(self, header, entries) -> None:
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id, balance, discount) -> None:
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model, length, max_speed, bidirectional) -> None:
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional
# Write your solution here:
class LunchCard:
    def __init__(self, balance) -> None:
        self.balance = balance
    
    def eat_lunch(self):
        if self.balance > 2.6:
            self.balance -= 2.6
    
    def eat_special(self):
        if self.balance > 4.6:
            self.balance -= 4.6

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount
    
    def __str__(self) -> str:
        return f"The balance is {self.balance:.1f} euros"
    
peter_card = LunchCard(20)
grace_card = LunchCard(30)
    
peter_card.eat_special()
grace_card.eat_lunch()
    
print("Peter: " + str(peter_card))
print("Grace: " + str(grace_card))

peter_card.deposit_money(20)
grace_card.eat_special()

print("Peter: " + str(peter_card))
print("Grace: " + str(grace_card))

peter_card.eat_lunch()
peter_card.eat_lunch()

grace_card.deposit_money(50)

print("Peter: " + str(peter_card))
print("Grace: " + str(grace_card))

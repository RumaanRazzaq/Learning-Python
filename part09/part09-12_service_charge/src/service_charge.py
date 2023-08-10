# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name, account_num, balance) -> None:
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount:float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance *= 0.99

    def __str__(self) -> str:
        pass
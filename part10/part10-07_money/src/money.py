# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __get_money(self):
        return self.__euros + (self.__cents/100)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another: 'Money'):
        return self.__get_money() == another.__get_money()

    def __lt__(self, another: 'Money'):
        return self.__get_money() < another.__get_money()

    def __gt__(self, another: 'Money'):
        return self.__get_money() > another.__get_money()

    def __ne__(self, another: 'Money'):
        return self.__get_money() != another.__get_money()

    def __add__(self, another: 'Money'):
        total___euros = self.__euros + another.__euros
        total___cents = self.__cents + another.__cents
        if total___cents >= 100:
            total___euros += 1
        total___cents = total___cents % 100
        new = Money(total___euros, total___cents)
        return new

    def __sub__(self, another: 'Money'):
        if (self.__get_money() < another.__get_money()):
            raise ValueError('a negative result is not allowed')
        total___euros = self.__euros - another.__euros
        if self.__cents >= another.__cents:
            total___cents = self.__cents - another.__cents
        else:
            total___euros -= 1
            total___cents = self.__cents + (100-another.__cents)
        new = Money(total___euros, total___cents)
        return new
    
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
# Write your solution here:
class Item:
    def __init__(self, name, weight) -> None:
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, weight) -> None:
        self.__max_weight  = weight
        self.__items = []

    def add_item(self, item):
        if self.weight() + item.weight() > self.__max_weight:
            i = 0
        else:
            self.__items.append(item)
    
    def weight(self):
        t_weight = 0
        for item in self.__items:
            t_weight += item.weight()
        return t_weight
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        heaviest = 0
        heaviest_item = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest:
                heaviest = item.weight()
                heaviest_item = item
        return heaviest_item

    def __str__(self) -> str:
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"    
        return f"{len(self.__items)} items ({self.weight()} kg)"
    
class CargoHold:
    def __init__(self, weight) -> None:
        self.__max_weight  = weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() > self.__max_weight:
            i = 0
        else:
            self.__suitcases.append(suitcase)
    
    def weight(self):
        t_weight = 0
        for suitcase in self.__suitcases:
            t_weight += suitcase.weight()
        return t_weight
    
    def capacity(self):
        return self.__max_weight - self.weight()
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self) -> str:
        if len(self.__suitcases) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.capacity()} kg"  
        return f"{len(self.__suitcases)} suitcases, space for {self.capacity()} kg"
    
if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")
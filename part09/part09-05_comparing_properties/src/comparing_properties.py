# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    
    def bigger(self, compared_to):
        if self.square_metres > compared_to.square_metres:
            return True
        return False

    def price_difference(self, compared_to):
        price_self = self.price_per_sqm * self.square_metres
        price_comparison = compared_to.price_per_sqm * compared_to.square_metres
        difference = price_self - price_comparison
        if difference < 0:
            return difference * -1
        return difference
    
    def more_expensive(self, compared_to):
        price_self = self.price_per_sqm * self.square_metres
        price_comparison = compared_to.price_per_sqm * compared_to.square_metres
        if price_self > price_comparison:
            return True
        return False
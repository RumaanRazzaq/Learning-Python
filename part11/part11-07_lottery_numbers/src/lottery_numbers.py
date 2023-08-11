# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_no, lottery) -> None:
        self.week_no = week_no
        self.__numbers = lottery
    
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__numbers])
    
    def hits_in_place(self, numbers):
        return [number if number in self.__numbers else -1 for number in numbers]
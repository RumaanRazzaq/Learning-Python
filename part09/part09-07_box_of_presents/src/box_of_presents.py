# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
    
    def __str__(self) -> str:
        return f"Present: {self.name} ({self.weight} kg)"
    
class Box:
    def __init__(self) -> None:
        self.present_list = []
    
    def add_present(self, present: Present):
        self.present_list.append(present)
    
    def total_weight(self):
        sum = 0
        for present in self.present_list:
            sum += present.weight
        return sum
# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self) -> None:
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if len(self.people) == 0:
            return True
        return False
    
    def print_contents(self):
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")
        
    def shortest(self):
        if len(self.people) == 0:
            return None
        shortest = self.people[0].height
        name = self.people[0]
        for person in self.people:
            if person.height < shortest:
                shortest = person.height
                name = person
        return name
    
    def remove_shortest(self):
        if len(self.people) == 0:
            return None
        shortest = self.people[0].height
        name = self.people[0]
        i = 0
        for person in self.people:
            if person.height < shortest:
                shortest = person.height
                name = person
        self.people.remove(name)
        return name
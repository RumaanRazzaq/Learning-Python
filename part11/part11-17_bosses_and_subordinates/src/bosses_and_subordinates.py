# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    sub = 0

    for emp in employee.subordinates:
        sub += 1
        sub += count_subordinates(emp)
    
    return sub
# Write your solution here:
class Task:
    total_tasks = 0
    def __init__(self, description, programmer, workload) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        Task.total_tasks += 1
        self.id = Task.total_tasks
    
    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True
    
    def __str__(self) -> str:
        if self.is_finished():
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

class OrderBook:
    def __init__(self) -> None:
        self.__tasks = []

    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.__tasks
    
    def mark_finished(self, id: int):
        for order in self.__tasks:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError
    
    def finished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == True]

    def unfinished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == False]
    
    def programmers(self):
        return list(set([order.programmer for order in self.__tasks]))
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f'No such {programmer} exists')
        
        tasks = [task for task in self.__tasks if task.programmer == programmer]
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0

        for task in tasks:
            if task.is_finished():
                finished += 1
                finished_workload += task.workload
            else:
                unfinished += 1
                unfinished_workload += task.workload

        return (finished, unfinished, finished_workload, unfinished_workload)
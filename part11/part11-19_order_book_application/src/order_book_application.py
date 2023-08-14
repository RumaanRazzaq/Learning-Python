# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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
                finished_workload += int(task.workload)
            else:
                unfinished += 1
                unfinished_workload += int(task.workload)

        return (finished, unfinished, finished_workload, unfinished_workload)
    
class OrderBookApplication:
    def __init__(self) -> None:
        self.__orders = OrderBook()

    def options(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        print()

    def add_order(self):
        desc = input("description: ")
        programmer = input("programmer and workload estimate: ")
        list = programmer.split(" ")
        try:
            num = int(list[1])
        except:
            print("erroneous input")
            return
        self.__orders.add_order(desc, list[0], list[1])
        print("added!")
        print()

    def finished_tasks(self):
        orders = self.__orders.finished_orders()
        if len(orders) == 0:
            print("no finished tasks")
        for order in orders:
            print(f"{order.id}: {order.description} ({order.workload} hours), programmer {order.programmer} FINISHED")
        print()

    def unfinished_tasks(self):
        orders = self.__orders.unfinished_orders()
        if len(orders) == 0:
            print("no unfinished tasks")
        for order in orders:
            print(f"{order.id}: {order.description} ({order.workload} hours), programmer {order.programmer} NOT FINISHED")
        print()

    def mark_as_finished(self):
        task_id = input("id: ")
        try:
            task_id = int(task_id)
        except:
            print("erroneous input")
            return
        if task_id > len(self.__orders.all_orders()):
                print("erroneous input")
                return
        self.__orders.mark_finished(task_id)
        print("marked as finished")
        print()
    
    def programmers(self):
        names = self.__orders.programmers()
        for name in names:
            print(name)
        print()
    
    def programmer_status(self):
        name = input("programmer: ")
        programmer_names = self.__orders.programmers()
        if name not in programmer_names:
            print("erroneous input")
            return
        list = self.__orders.status_of_programmer(name)
        print(f"tasks: finished {list[0]} not finished {list[1]}, hours: done {list[2]} scheduled {list[3]}")
        print()

    def start(self):
        self.options()

        while True:
            command_no = int(input("command: "))
            if command_no == 0:
                break
            elif command_no == 1:
                self.add_order()
            elif command_no == 2:
                self.finished_tasks()
            elif command_no == 3:
                self.unfinished_tasks()
            elif command_no == 4:
                self.mark_as_finished()
            elif command_no == 5:
                self.programmers()
            elif command_no == 6:
                self.programmer_status()
    
application = OrderBookApplication()
application.start()
class Task:
    def __init__(self, name):
        self.name = name

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class CircularTaskList:
    def __init__(self):
        self.tail = None  

    def add_task(self, name):
        new_node = Node(Task(name))
        if not self.tail:
            self.tail = new_node
            self.tail.next = new_node  
        else:
            new_node.next = self.tail.next  
            self.tail.next = new_node      
            self.tail = new_node            

    def show_tasks(self):
        if not self.tail:
            print("No tasks to show.")
            return

        current = self.tail.next  # Start from head
        print("Today's Circular Task List:")
        while True:
            print(f"- {current.task.name}")
            current = current.next
            if current == self.tail.next:
                break

    def simulate_day(self, rounds):
        if not self.tail:
            print("No tasks to run.")
            return

        current = self.tail.next
        print("Daily Task Loop:")
        for i in range(rounds):
            print(f"Round {i+1}: {current.task.name}")
            current = current.next
tasks = CircularTaskList()
tasks.add_task("Wake up")
tasks.add_task("Exercise")
tasks.add_task("Study")
tasks.add_task("Relax")
tasks.add_task("Sleep")
tasks.show_tasks()
print("\n--- Simulating Task Loop ---\n")
tasks.simulate_day(8)

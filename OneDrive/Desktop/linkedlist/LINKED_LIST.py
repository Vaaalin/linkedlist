
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None
class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, name, priority):
        new_task = Task(name, priority)
        new_node = Node(new_task)
        new_node.next = self.head
        self.head = new_node

    def print_tasks(self):
        current = self.head
        print("Today's Tasks:")
        while current:
            print(f"- {current.task.name} (Priority {current.task.priority})")
            current = current.next
todo = TaskList()
todo.add_task("Study for math test", 1)
todo.add_task("Complete science homework", 2)
todo.add_task("Attend history class", 3)

todo.print_tasks()

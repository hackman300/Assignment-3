from node import Node
import time

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def print_stack(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

undo_stack = Stack()
redo_stack = Stack()

while True:
        print("\nUndo/Redo System")
        print("1. Perform Action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            action = input("Enter the action to perform: ")
            undo_stack.push(action)
            redo_stack = Stack()
            print(f"Performed action: {action}")
        elif choice == '2':
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Action undid: {action}")
            else:
                print("Nothing to undo")
        elif choice == '3':
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Action redid: {action}")
            else:
                print("Nothing to redo")
        elif choice == '4':
            print("Undo Stack:")
            undo_stack.print_stack()
        elif choice == '5':
            print("Redo Stack:")
            redo_stack.print_stack()
        elif choice == '6':
            print("Exiting system...")
            time.sleep(2)
            print("System Exited")
            break
        else:
            print("Invalid choice")

from node import Node
import time

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

def run_help_desk():
    queue = Queue()

    while True:
            print("\n*** Help Desk Ticketing System ***")
            print("1. Add customer")
            print("2. Help next customer")
            print("3. View next customer")
            print("4. View all waiting customers")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                name = input("Enter customer name: ")
                queue.enqueue(name)
                print(f"{name} added to the queue.")
            elif choice == "2":
                name = queue.dequeue()
                if name is None:
                    print("No customers waiting.")
                else:
                    print(f"{name} has been helped")

            elif choice == "3":
                name = queue.peek()
                if name is None:
                    print("No customers waiting.")
                else:
                    print(f"Next customer: {name}")

            elif choice == "4":
                print("Waiting customers:")
                if queue.is_empty():
                    print("No customers waiting.")
                else:
                    current = queue.front
                    while current:
                        print(current.value)
                        current = current.next

            elif choice == "5":
                print("Exiting Help Desk System...")
                time.sleep(2)
                print("System Exited")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

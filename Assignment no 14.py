class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item (unsafe if empty)."""
        return self.items.pop()

    def safe_pop(self):
        """Safely remove the top item, handling empty stack."""
        if not self.items:
            print("Stack is empty, nothing to pop.")
            return None
        return self.items.pop()

    def peek(self):
        """View the top item without removing it."""
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


def main():
    stack = Stack()

    # Demonstration
    print("Pushing items: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack size:", stack.size())
    print("Top element:", stack.peek())

    print("\nPerforming safe pops:")
    print("Popped:", stack.safe_pop())
    print("Popped:", stack.safe_pop())
    print("Popped:", stack.safe_pop())
    print("Popped:", stack.safe_pop())  # This will trigger the safe empty message

    print("Final stack size:", stack.size())


if __name__ == "__main__":
    main()

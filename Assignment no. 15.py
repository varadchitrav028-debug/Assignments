from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item (unsafe if empty)."""
        return self.items.popleft()

    def safe_dequeue(self):
        """Safely remove the front item, handling empty queue."""
        if not self.items:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.items.popleft()

    def peek(self):
        """View the front item without removing it."""
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


def main():
    queue = Queue()

    print("Enqueuing items: A, B, C")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print("Queue size:", queue.size())
    print("Front element:", queue.peek())

    print("\nPerforming safe dequeues:")
    print("Dequeued:", queue.safe_dequeue())
    print("Dequeued:", queue.safe_dequeue())
    print("Dequeued:", queue.safe_dequeue())
    print("Dequeued:", queue.safe_dequeue())  # This will trigger the safe empty message

    print("Final queue size:", queue.size())


if __name__ == "__main__":
    main()

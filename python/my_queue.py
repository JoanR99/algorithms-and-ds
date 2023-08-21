from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        self.length += 1

        node = Node(item)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> int:
        if self.head is None:
            raise Exception("Dequeueing from empty queue")

        self.length -= 1
        value = self.head.value

        if self.length == 0:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return value

    def peek(self) -> int:
        if self.head is None:
            raise Exception("Dequeueing from empty queue")

        return self.head.value


my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(9)
my_queue.enqueue(2)
my_queue.enqueue(4)
print(my_queue.dequeue())
print(my_queue.length)

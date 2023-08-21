from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.prev: Optional[Node] = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, value):
        self.length += 1

        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            self.head.prev = newNode
            self.head = newNode

    def pop(self) -> int:
        if self.head is None:
            raise Exception("Popping from an empty stack")

        self.length = max(0, self.length - 1)

        value = self.head.value

        if self.length == 0:
            self.head = None
        else:
            self.head = self.head.prev

        return value

    def peek(self) -> int:
        if self.head is None:
            raise Exception("Popping from an empty stack")

        return self.head.value


my_stack = Stack()
my_stack.push(5)
my_stack.push(4)
my_stack.push(9)
my_stack.push(7)
print(my_stack.pop())
print(my_stack.length)

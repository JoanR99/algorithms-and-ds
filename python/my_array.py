from typing import Any

class MyArray:
    length: int
    data: dict[int, Any]

    def __init__(self):
        self.length = 0
        self.data = {}

    def push(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        item = self.data.get(self.length - 1, None)
        self.data.pop(self.length - 1)
        return item

    def delete(self, index: int):
        item = self.data[index]
        self.shift(index)
        return item

    def shift(self, index: int):
        i = index

        while i < self.length:
            self.data[i] = self.data.get((i + 1), None)
            i += 1
        self.data.pop(self.length-1)
        self.length -= 1

number_array = MyArray()
number_array.push(1)
number_array.push(2)
number_array.push(3)
number_array.delete(1)
print(number_array.length)
print(number_array.data)

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.size_of_stack() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size_of_stack(self):
        return len(self.stack)


stack = Stack()
stack.push(2)
stack.push(5)
stack.push(9)
stack.push(12)
print("Size of stack : ", stack.size_of_stack())
print("Item popped : ", stack.pop())
print("Size of stack : ", stack.size_of_stack())
print("Item peeked : ", stack.peek())

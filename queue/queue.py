class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    # O(N) run time, solution? -> Doubly Linked List
    def dequeue(self):
        if self.size_of_queue() < 1:
            return
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return self.queue == []

    def size_of_queue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(9)
queue.enqueue(12)
print("Size of stack : ", queue.size_of_queue())
print("Item dequeued : ", queue.dequeue())
print("Size of stack : ", queue.size_of_queue())
print("Item peeked : ", queue.peek())

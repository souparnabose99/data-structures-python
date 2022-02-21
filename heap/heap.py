
CAPACITY = 10


class Heap:

    def __init__(self):
        self.heap_size = 0
        self.heap = [0]*CAPACITY

    def insert(self, item):

        # when heap is full
        if self.heap_size == CAPACITY:
            return
        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check heap properties
        self.fix_heap(self.heap_size-1)

    # starting with actual node inserted to root node, compare values for swap operations-> log(N) operations, O(log(N))
    def fix_heap(self, index):
        # for node with index i, left child has index = 2i+1, right child has index 2i+1
        # hence, reverse the eqn-> l = 2i+1, r = 2i+2-> i=l-1/2
        parent_index = (index - 1)//2
        # now consider all items above til root node, if heap prop is violated then swap parent with child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_heap(parent_index)

    def get_max_item(self):
        return self.heap[0]

    # return the max element and remove it from the heap
    def poll_heap(self):
        max_item = self.get_max_item()

        # swap the root with the last item
        self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.heap_size -= 1

        # now perform heapify operation
        self.heapify(0)
        return max_item

    # start from root node and rearrange heap to make sure heap properties are not violated, O(log(N))
    def heapify(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        largest_index = index

        # look for the largest(parent or left node)
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left
        # if right child > left child, then largest_index = right child
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index]:
            largest_index = index_right

        # If parent larger than child: it is valid heap and we terminate all recursive calls further
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.heapify(largest_index)

    # O(Nlog(N)) -> N items and O(logN) for poll_heap operation
    def heap_sort(self):

        for _ in range(self.heap_size):
            max_item = self.poll_heap()
            print(max_item)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)
    heap.insert(100)

    print(heap.heap)

    print("----------------------------")
    heap.heap_sort()






import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.no_of_nodes = 0

    # O(1) for insertion at the start of LL
    def insert_at_start(self, data):
        self.no_of_nodes = self.no_of_nodes + 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node


if __name__ == "__main__":
    linked_list = LinkedList()
    start = time.time()
    for i in range(500000):
        linked_list.insert_at_start(i)
    print("Insertion time for Linked List in seconds : ", str(time.time() - start))

    arr = []
    start = time.time()
    for i in range(500000):
        arr.insert(0, i)
    print("Insertion time for Array in seconds : ", str(time.time() - start))

# Output:
# Insertion time for Linked List in seconds :  1.0503969192504883
# Insertion time for Array in seconds :  98.33773922920227

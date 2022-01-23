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

    # O(N) for insertion at the end of LL
    def insert_at_end(self, data):
        self.no_of_nodes = self.no_of_nodes + 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    # O(1)
    def size_of_ll(self):
        return self.no_of_nodes

    # O(N)
    def traverse_ll(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def remove_from_ll(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # Item not present in Linked List
        if actual_node is None:
            return

        # Decrease node count for deletion
        self.no_of_nodes = self.no_of_nodes - 1

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node


ll = LinkedList()
ll.insert_at_start(15)
ll.insert_at_start(8)
ll.insert_at_start(5)
ll.insert_at_end(6)
ll.insert_at_start("Yo")
ll.traverse_ll()
print("Size : ", ll.size_of_ll())
ll.remove_from_ll(8)
print("---------")
ll.traverse_ll()
print("Size : ", ll.size_of_ll())



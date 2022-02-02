class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.no_of_nodes = 0

    # Inserts at end for O(1) runtime complexity as references already present
    def insert(self, data):
        new_node = Node(data)
        self.no_of_nodes = self.no_of_nodes + 1

        # when ll is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the ll
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous

    def remove_from_ll(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next

        if actual_node is None:
            return

        self.no_of_nodes = self.no_of_nodes - 1

        if previous_node is None:
            self.head = actual_node.next
        else:
            previous_node.next = actual_node.next



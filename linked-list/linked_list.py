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

    # O(N) runtime complexity
    def find_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer.data
    
    #O(N) runtime complexity
    def reverse_ll_in_place(self):
        previous_node = None
        current_node = self.head
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
        return


ll = LinkedList()
ll.insert_at_start(15)
ll.insert_at_start(8)
ll.insert_at_start(5)
ll.insert_at_end(6)
ll.insert_at_end(76)
ll.insert_at_end(43)
ll.insert_at_start("Yo")
ll.traverse_ll()
print("Size : ", ll.size_of_ll())
# ll.remove_from_ll(8)
print("---------")
# ll.traverse_ll()
print("Size : ", ll.size_of_ll())
print(ll.find_middle_node())
ll.reverse_ll_in_place()
ll.traverse_ll()



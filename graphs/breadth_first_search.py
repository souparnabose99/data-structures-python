
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def bfs(start_node):
    # keep iterating through all neighbours until queue becomes empty
    queue = [start_node]
    while queue:
        # remove and return the first item into the list
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        # consider neighbours of actual node 1 by 1
        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node3.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)
    node4.adjacency_list.append(node6)

    # run BFS
    bfs(node1)




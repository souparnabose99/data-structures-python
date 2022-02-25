
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def dfs(start_node):
    # LIFO structure needed
    stack = [start_node]

    # Iterate until stack becomes empty
    while stack:
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            # If the node has not been visited, we insert the item into the stack
            if not n.visited:
                stack.append(n)


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

    # run DFS
    dfs(node1)


    

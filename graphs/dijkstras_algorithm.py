import heapq


class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Vertex:

    def __init__(self, name):
        self.name = name
        self.visited = False
        # this is the node where we came from in the shortest path
        self.predecessor = None
        # this is how we store the children
        self.adjacency_list = []
        # this is the minimum distance (shortest path) from the source to target vertex
        self.min_distance = float('inf')

    # this is how python compares objects
    # insert objects into heap and compare objects
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance


class DijkstrasAlgorithm:

    def __init__(self):
        # this is a heap representation using heapq (binary heap)
        self.heap = []

    def calculate(self, start_vertex):
        # initialize vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        

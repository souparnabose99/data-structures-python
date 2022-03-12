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

        # iterate until heap is not empty
        while self.heap:
            # pop the vertex with lowest min distance parameter
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            # consider neighbours
            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                # compare min distance
                new_distance = u.min_distance + edge.weight

                # there is a shorter path to v
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance

                    # Lazy implementation
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        print("Shortest path to the vertex is : ", vertex.min_distance)
        actual_vertex = vertex

        while actual_vertex.predecessor is not None:
            print("Vertex Name: ", actual_vertex.name)
            actual_vertex = actual_vertex.predecessor

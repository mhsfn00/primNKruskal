import sys

class GraphKruskal:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # Default dictionary to store graph

    # Function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):

        # This will store the resultant MST
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort edges in increasing order on basis of cost
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Spanning Tree edges
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                e = e + 1

        # Calculate the total weight of the MST
        total_weight = sum(weight for _, _, weight in result)

        # Print the contents of result[] to display the
        # constructed MST and the total weight
        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))
        print("Total weight of the MST:", total_weight)

class GraphPrim:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def minDistance(self, dist, sptSet):
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def printMST(self, parent, n, total_weight):
        print("Edge \tWeight")
        for i in range(1, n):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print("Total weight of the MST:", total_weight)

    def primMST(self):
        parent = [None] * self.V
        key = [sys.maxsize] * self.V
        mstSet = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for cout in range(self.V):
            u = self.minDistance(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        total_weight = sum(key[i] for i in range(1, self.V))

        self.printMST(parent, self.V, total_weight)

if __name__ == '__main__':
    gk = GraphKruskal(4)
    gk.add_edge(0, 1, 10)
    gk.add_edge(0, 2, 6)
    gk.add_edge(0, 3, 5)
    gk.add_edge(1, 3, 15)
    gk.add_edge(2, 3, 4)

    gkk = GraphKruskal(5)
    gkk.add_edge(0, 1, 2)
    gkk.add_edge(0, 3, 6)
    gkk.add_edge(1, 2, 3)
    gkk.add_edge(1, 3, 8)
    gkk.add_edge(1, 4, 5)
    gkk.add_edge(2, 4, 7)

    gkk.kruskal_mst()

    gp = GraphPrim(5)
    gp.add_edge(0, 1, 2)
    gp.add_edge(0, 3, 6)
    gp.add_edge(1, 2, 3)
    gp.add_edge(1, 3, 8)
    gp.add_edge(1, 4, 5)
    gp.add_edge(2, 4, 7)
    gp.primMST()
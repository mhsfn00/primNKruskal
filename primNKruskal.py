import sys

class GraphKruskal:
    def __init__(self):
        self.graph = []
        self.vertex_map = {}
        self.reverse_map = {}
        self.next_index = 0

    def add_vertex(self, name):
        if name not in self.vertex_map:
            self.vertex_map[name] = self.next_index
            self.reverse_map[self.next_index] = name
            self.next_index += 1

    def add_edge(self, u_name, v_name, w):
        u = self.vertex_map[u_name]
        v = self.vertex_map[v_name]
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(len(self.vertex_map)):
            parent.append(node)
            rank.append(0)

        while e < len(self.vertex_map) - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                e = e + 1

        total_weight = sum(weight for _, _, weight in result)

        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            u_name = self.reverse_map[u]
            v_name = self.reverse_map[v]
            print("%s -- %s == %d" % (u_name, v_name, weight))
        print("Total weight of the MST:", total_weight)

        # Convert result to use vertex names instead of indices
        mst_edges = []
        for u, v, weight in result:
            u_name = self.reverse_map[u]
            v_name = self.reverse_map[v]
            mst_edges.append((u_name, v_name, weight))

        return mst_edges

class GraphPrim:
    def __init__(self):
        self.graph = {}
        self.vertex_map = {}
        self.reverse_map = {}
        self.next_index = 0

    def add_vertex(self, name):
        if name not in self.vertex_map:
            self.vertex_map[name] = self.next_index
            self.reverse_map[self.next_index] = name
            self.next_index += 1
            self.graph[self.next_index-1] = {} 

    def add_edge(self, u_name, v_name, w):
        u = self.vertex_map[u_name]
        v = self.vertex_map[v_name]
        self.graph[u][v] = w
        self.graph[v][u] = w

    def minDistance(self, dist, sptSet):
        min_val = sys.maxsize
        min_index = -1

        for v_index in self.graph:
            v_name = self.reverse_map[v_index]
            if dist[v_index] < min_val and not sptSet[v_index]:
                min_val = dist[v_index]
                min_index = v_index

        return min_index

    def printMST(self, parent, total_weight):
        print("Edge \tWeight")
        for i_index in self.graph:
            i_name = self.reverse_map.get(i_index)
            if i_name is None:
                continue
            if parent[i_index] is not None and parent[i_index] != -1:  
                parent_name = self.reverse_map.get(parent[i_index]) 
                if parent_name is None:
                    continue 
                print(f"{parent_name} - {i_name}\t{self.graph.get(i_index, {}).get(parent[i_index])}") # Use get to avoid KeyError
        print("Total weight of the MST:", total_weight)

    def primMST(self):
        num_vertices = len(self.vertex_map)
        parent = [None] * num_vertices
        key = [sys.maxsize] * num_vertices
        mstSet = [False] * num_vertices

        start_vertex_index = 0
        key[start_vertex_index] = 0
        parent[start_vertex_index] = -1

        for _ in range(num_vertices):
            u_index = self.minDistance(key, mstSet)

            if u_index == -1:
                continue

            mstSet[u_index] = True

            for v_index in self.graph:  
                if self.graph.get(u_index) and self.graph[u_index].get(v_index) and self.graph[u_index][v_index] > 0 and not mstSet[v_index] and key[v_index] > self.graph[u_index][v_index]:
                    key[v_index] = self.graph[u_index][v_index]
                    parent[v_index] = u_index

        total_weight = sum(key[i] for i in range(num_vertices) if parent[i] is not None)

        self.printMST(parent, total_weight)

        # Build and return the MST as a list of edges
        mst_edges = []
        for i_index in self.graph:
            i_name = self.reverse_map.get(i_index)
            if i_name is None:
                continue
            if parent[i_index] is not None and parent[i_index] != -1:
                parent_name = self.reverse_map.get(parent[i_index])
                if parent_name is None:
                    continue
                weight = self.graph[i_index][parent[i_index]]
                mst_edges.append((parent_name, i_name, weight))

        return mst_edges

def readInputsNMakeGraphs():
    try:
        with open(entrada, "r") as file:
            graphInput = file.readlines()
            print('File read successfuly')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Getting quantity of vertices
    vertices = graphInput[0].strip()

    gp = GraphPrim()
    gk = GraphKruskal()

    for vertice in vertices:
        if (vertice != ' '):
            gp.add_vertex(f'{vertice}')
            gk.add_vertex(f'{vertice}')

    for edge in range(1, len(graphInput)):
        info = graphInput[edge].strip()
        verVerWeight = info.split()
        verVerWeight[2] = int(verVerWeight[2])
        gp.add_edge(verVerWeight[0], verVerWeight[1], verVerWeight[2])
        gk.add_edge(verVerWeight[0], verVerWeight[1], verVerWeight[2])
    
    return gk, gp

def writeOutput(kruskalMST, primMST):   
    kruskalWeight = 0
    primWeight = 0

    with open(saidaKru, 'w') as file:
        for connection in kruskalMST:
            file.write(f'{connection[0]} {connection[1]} {connection[2]}\n')
            kruskalWeight += connection[2]
        file.write(f'custo_total = {kruskalWeight}')

    with open(saidaPrim, 'w') as file:
        for connection in primMST:
            file.write(f'{connection[0]} {connection[1]} {connection[2]}\n')
            primWeight += connection[2]
        file.write(f'custo_total = {primWeight}')
    
    print('Output written successfuly')

entrada = 'entrada.txt'
saidaPrim = 'saida.pri'
saidaKru = 'saida.kru'

gk, gp = readInputsNMakeGraphs()
primMST = gp.primMST()
kruskalMST = gk.kruskal_mst()
writeOutput(kruskalMST, primMST)
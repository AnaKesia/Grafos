from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # grafo representado como um dicionário de adjacência
        self.V = vertices  # número de vértices
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))  # adiciona uma aresta do vértice u para o vértice v com capacidade w
    
    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.pop(0)
            
            for v, capacity in self.graph[u]:
                if visited[v] == False and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    
                    if v == t:
                        return True
        
        return False
    
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            
            while s != source:
                for v, capacity in self.graph[parent[s]]:
                    if v == s:
                        path_flow = min(path_flow, capacity)
                s = parent[s]
            
            max_flow += path_flow
            
            v = sink
            while v != source:
                u = parent[v]
                for idx, (vertex, capacity) in enumerate(self.graph[u]):
                    if vertex == v:
                        self.graph[u][idx] = (vertex, capacity - path_flow)
                for idx, (vertex, capacity) in enumerate(self.graph[v]):
                    if vertex == u:
                        self.graph[v][idx] = (vertex, capacity + path_flow)
                v = parent[v]
        
        return max_flow

# Exemplo de uso:
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source = 0
sink = 5
print(f"O fluxo máximo é {g.ford_fulkerson(source, sink)}")

g = Graph(5)  # Temos 5 vértices: A, B, C, D, E
g.add_edge(0, 1, 10)  # A (0) -> B (1) com capacidade 10
g.add_edge(0, 2, 5)   # A (0) -> C (2) com capacidade 5
g.add_edge(1, 2, 15)  # B (1) -> C (2) com capacidade 15
g.add_edge(1, 3, 10)  # B (1) -> D (3) com capacidade 10
g.add_edge(2, 4, 10)  # C (2) -> E (4) com capacidade 10
g.add_edge(3, 4, 10)  # D (3) -> E (4) com capacidade 10

source = 0  # Fonte: A (índice 0)
sink = 4    # Sumidouro: E (índice 4)

print(f"O fluxo máximo é {g.ford_fulkerson(source, sink)}")


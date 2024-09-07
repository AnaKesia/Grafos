import heapq  # Para a fila de prioridade
from collections import defaultdict 

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = defaultdict(list)  # Grafo como um dicionário de listas
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # Adiciona aresta u -> v com peso
    
    def dijkstra(self, src):
        # Inicializa as distâncias como infinito, exceto a fonte
        dist = {i: float('inf') for i in range(self.V)}
        dist[src] = 0
        
        # Fila de prioridade para selecionar o próximo vértice com menor distância
        pq = [(0, src)]  # (distância, vértice)
        
        while pq:
            current_dist, u = heapq.heappop(pq)  # Extrai o vértice com menor distância
            
            # Se a distância atual é maior que a registrada, continuamos (verificação de relaxamento)
            if current_dist > dist[u]:
                continue
            
            # Para todos os vizinhos v de u
            for v, weight in self.graph[u]:
                distance = current_dist + weight  # Cálculo da nova distância
                
                # Se encontrarmos uma distância menor, atualizamos
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))  # Inserimos o vizinho na fila com a nova distância
        
        return dist  # Retorna as distâncias do vértice de origem para todos os outros

# Criando o grafo
g = Graph(6)  # 6 vértices: A, B, C, D, E, F
g.add_edge(0, 1, 3)  # A -> B com peso 3
g.add_edge(0, 3, 2)  # A -> D com peso 2
g.add_edge(1, 2, 1)  # B -> C com peso 1
g.add_edge(1, 4, 3)  # B -> E com peso 3
g.add_edge(3, 4, 6)  # D -> E com peso 6
g.add_edge(2, 4, 5)  # C -> E com peso 5
g.add_edge(4, 5, 2)  # E -> F com peso 2

# Executando o algoritmo de Dijkstra a partir do vértice A (índice 0)
distances = g.dijkstra(0)
print(distances)  # Exibindo as distâncias do vértice A para todos os outros

g = Graph(5)  # Cria um grafo com 5 vértices
g.add_edge(0, 1, 9)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(0, 4, 3)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 4)

distances = g.dijkstra(0)
print(distances)
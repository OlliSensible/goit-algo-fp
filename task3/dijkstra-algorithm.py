import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

G = nx.Graph()

vertices = ["Alice", "Bob", "Charlie", "David", "Eve"]
G.add_nodes_from(vertices)

edges = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "David"), ("David", "Eve")]
for u, v in edges:
    G.add_edge(u, v, weight=random.randint(1, 10))

def draw_graph_with_weights(graph):
    pos = nx.spring_layout(graph) 
    edge_labels = nx.get_edge_attributes(graph, 'weight')  
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=15)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

draw_graph_with_weights(G)
plt.show()

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)] 

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight 

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

shortest_paths = dijkstra(G, "Alice")
print("Найкоротші шляхи від Alice:", shortest_paths)
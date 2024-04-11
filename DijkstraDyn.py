

def dijkstradyn(graph, start, end=None):
    # Diccionarios para almacenar las distancias más cortas y los nodos anteriores
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    predecessor = {}
    unseen_nodes = set(graph.keys())
    
    while unseen_nodes:
        # Selecciona el nodo no visto con la distancia más corta
        current_node = min(unseen_nodes, key=lambda node: shortest_distances[node])
        
        # Si el nodo actual es el nodo final, termina
        if current_node == end:
            break
        
        unseen_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            new_distance = shortest_distances[current_node] + weight
            # If a shorter path to the neighbor is found
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                predecessor[neighbor] = current_node

    # Recontrsuye el camino más corto con los nodos anteriores
    path = []
    current_node = end
    while current_node != start:
        if current_node in predecessor:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        else:
            print("Path not reachable.")
            return None, None
    path.insert(0, start)
    
    return shortest_distances[str(len(shortest_distances)-1)], path


#Función para gráficar el grafo
    
def showgraph(graph):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold', font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

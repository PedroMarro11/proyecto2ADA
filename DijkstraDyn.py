

def dijkstra(graph, start, end):
    # Initialize dictionaries for shortest distance and tracking the visited nodes
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    predecessor = {}
    unseen_nodes = set(graph.keys())
    
    while unseen_nodes:
        # Select the unvisited node with the smallest distance
        current_node = min(unseen_nodes, key=lambda node: shortest_distances[node])
        
        # Break out of the loop if the end node is reached
        if current_node == end:
            break
        
        unseen_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            new_distance = shortest_distances[current_node] + weight
            # If a shorter path to the neighbor is found
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                predecessor[neighbor] = current_node

    # Reconstruct the shortest path from start to end
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
    
    return shortest_distances[end], path

# Example usage:
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'E': 3, 'F': 4},
    'D': {'B': 10, 'G': 11},
    'E': {'C': 3, 'F': 6, 'H': 5},
    'F': {'C': 4, 'E': 6, 'G': 2},
    'G': {'D': 11, 'F': 2, 'I': 2, 'H': 10},
    'H': {'E': 5, 'G': 10, 'I': 3, 'J': 5},
    'I': {'G': 2, 'H': 3, 'J': 3},
    'J': {'H': 5, 'I': 3}
}

start_node = 'A'
end_node = 'J'
shortest_distance, path = dijkstra(graph, start_node, end_node)
print("Shortest distance to", end_node, ":", shortest_distance)
print("Path:", path)


dijkstra(graph, 'A', 'D')

#show graph graphically
    
def showgraph():
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
showgraph()
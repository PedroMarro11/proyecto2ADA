def DijkstraGreedy(graph, start, end=None):
    # Initialize the distance from the start node to all other nodes
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0
    
    # Initialize the list of visited nodes
    visited = []

    # Initialize the list of nodes to visit
    nodes = list(graph)
    
    # While there are nodes to visit
    while nodes:
        # Select the node with the smallest distance
        #print(distance) #descomentar para observar funcionamiento 
        min_node = None
        for node in nodes:
            if min_node is None:
                min_node = node
            elif distance[node] < distance[min_node]:
                min_node = node

        if min_node == end:
            visited.append(min_node)
            break
        #print(min_node) #descomentar para observar funcionamiento
        # For each neighbor of the node
        for neighbor, weight in graph[min_node].items():
            # Calculate the new distance
            new_distance = distance[min_node] + weight
            
            # If the new distance is smaller than the current distance
            if new_distance < distance[neighbor]:
                # Update the distance
                distance[neighbor] = new_distance

        # Mark the node as visited
        visited.append(min_node)

        # Remove the node from the list of nodes to visit
        nodes.remove(min_node)

    return visited, distance[str(len(distance)-1)], distance


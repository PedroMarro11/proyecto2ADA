def DijkstraGreedy(graph, start, end=None):
    #Inicializa la distancia de los nodos
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0
    
    # Lista de los nodos visitados
    visited = []

    # Lista de nodos a visitar
    nodes = list(graph)
    
    # Mientras haya nodos por visitar
    while nodes:
        # Selecciona el nodo con la menos distancia
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
        # Para cada nodo vecino del nodo con la menor distancia
        for neighbor, weight in graph[min_node].items():
            # Calcular nueva distancia
            new_distance = distance[min_node] + weight
            
            # Si la nueva distancia es menor
            if new_distance < distance[neighbor]:
                # Actualizar distancia
                distance[neighbor] = new_distance

        # Agregar el nodo a la lista de nodos visitados
        visited.append(min_node)

        # remover el nodo de la lista de nodos a visitar
        nodes.remove(min_node)

    return visited, distance[str(len(distance)-1)], distance


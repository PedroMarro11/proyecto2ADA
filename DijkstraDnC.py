
import math 
def dijkstraDnCv2(graph, start, end = None):
    if start == end:
        return [start], 0
    #Caso Base
    if len(graph) == 2:
        x = list(graph)
        return x, graph[x[0]][x[1]]
    # Caso base 2
    if len(graph) == 1:
        return [start], 0
    
    graphTrue = graph.copy()
    min_dists = []
    nodes = []
    #Ecuentra los nodos con la menor distancia
    for node in graph:
        if node == start:
            continue
        dist = float('inf')
        for subnode in graph[node]:
            if subnode not in graph:
                continue
            if subnode == start:
                continue
            if graph[node][subnode] < dist:
                dist = graph[node][subnode]
                min_node = subnode
        min_dists.append(graph[node][min_node])
        nodes.append((node,min_node))
    
    sep = nodes[min_dists.index(min(min_dists))]
    
    
    # Parte en dos el grafo
    first_half = {start: graph.pop(start), sep[0]: graph.pop(sep[0])}
    second_half = {sep[1]: graph.pop(sep[1])}

    first_half = {**first_half, **dict(list(graph.items())[math.floor(len(graph) / 2)+1:])}
    second_half = {**second_half, **dict(list(graph.items())[:math.floor(len(graph) / 2)+1])}
     

    # Llamada recursiva a las dos mitades
    if end is None or end in first_half:
        left_distance = dijkstraDnCv2(first_half, start, end)
    else:
        left_distance = dijkstraDnCv2(first_half, start)
    
    if end is None or end in second_half:
        right_distance = dijkstraDnCv2(second_half, sep[1], end)
    else:
        right_distance = dijkstraDnCv2(second_half, sep[1])
    
    # Combina los resultados
    path = left_distance[0] + right_distance[0]
    total_distance = left_distance[1] + right_distance[1] + graphTrue[sep[0]][sep[1]]
    
    return path, total_distance




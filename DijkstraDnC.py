
import math 
def dijkstraDnCv2(graph, start, end = None):
    if start == end:
        return [start], 0
    #Base case: if just two nodes, return the nodes and the distance between them
    if len(graph) == 2:
        x = list(graph)
        return x, graph[x[0]][x[1]]
    # Base case: if just one node, return that node to visit and distance 0
    if len(graph) == 1:
        return [start], 0
    
    graphTrue = graph.copy()
    min_dists = []
    nodes = []
    #find nodes with smallest distance
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
    
    
    # Divide the graph into two halves
    first_half = {start: graph.pop(start), sep[0]: graph.pop(sep[0])}
    second_half = {sep[1]: graph.pop(sep[1])}

    first_half = {**first_half, **dict(list(graph.items())[math.floor(len(graph) / 2)+1:])}
    second_half = {**second_half, **dict(list(graph.items())[:math.floor(len(graph) / 2)+1])}
     

       # Recursively solve the left and right halves with consideration of end node
    if end is None or end in first_half:
        left_distance = dijkstraDnCv2(first_half, start, end)
    else:
        left_distance = dijkstraDnCv2(first_half, start)
    
    if end is None or end in second_half:
        right_distance = dijkstraDnCv2(second_half, sep[1], end)
    else:
        right_distance = dijkstraDnCv2(second_half, sep[1])
    
    # Combine the results from left and right halves
    path = left_distance[0] + right_distance[0]
    total_distance = left_distance[1] + right_distance[1] + graphTrue[sep[0]][sep[1]]
    
    return path, total_distance


# Example usage
graph1= {
    '0': {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7},
    '1': {'0': 1, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6},
    '2': {'0': 2, '1': 1, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5},
    '3': {'0': 3, '1': 2, '2': 1, '4': 1, '5': 2, '6': 3, '7': 4},
    '4': {'0': 4, '1': 3, '2': 2, '3': 1, '5': 1, '6': 2, '7': 3},
    '5': {'0': 5, '1': 4, '2': 3, '3': 2, '4': 1, '6': 1, '7': 2},
    '6': {'0': 6, '1': 5, '2': 4, '3': 3, '4': 2, '5': 1, '7': 1},
    '7': {'0': 7, '1': 6, '2': 5, '3': 4, '4': 3, '5': 2, '6': 1}
}




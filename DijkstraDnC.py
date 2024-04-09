
import math 
def dijkstraDnCv2(graph, start, end = None):
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
     

    # Recursively solve the left and right halves
    left_distance = dijkstraDnCv2(first_half, start, sep[0])
    right_distance = dijkstraDnCv2(second_half, sep[1])
    
    return left_distance[0]+right_distance[0], left_distance[1] + right_distance[1]+graphTrue[sep[0]][sep[1]] 


# Example usage
graph = {
    'A': {'B': 5, 'C': 3, "D":10},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4, "A":10}
}
a, b = dijkstraDnCv2(graph, "A")
print(a, b)
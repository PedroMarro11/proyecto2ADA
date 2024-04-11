import random

def generate_fully_connected_graphs_with_random_weights(n_nodes, n_graphs):
    graphs = []
    for _ in range(n_graphs):
        graph = {}
        for i in range(n_nodes):
            connections = {}
            for j in range(n_nodes):
                if i != j:
                    # Assigning random weights in the range 1 to 10
                    connections[str(j)] = random.randint(1, 10)
            graph[str(i)] = connections
        graphs.append(graph)
    return graphs

# Generate 1 fully connected graph with 16 nodes

graphs64 = generate_fully_connected_graphs_with_random_weights(64, 5)
graphs32 = generate_fully_connected_graphs_with_random_weights(32, 5)
graphs16 = generate_fully_connected_graphs_with_random_weights(16, 5)
graphs8 = generate_fully_connected_graphs_with_random_weights(8, 5)
graphs4 = generate_fully_connected_graphs_with_random_weights(4, 5)
graph2 = generate_fully_connected_graphs_with_random_weights(2, 5)


#export enumerate each graph like graph1 = {graph} for each graph in graphs2, graphs4, graphs8, graphs16, graphs32 and graphs64 to graphs.txt

def export_graphs(graphs, filename, a):
    with open(filename, 'w') as f:
        for i, graph in enumerate(graphs):
            f.write(f'graph{i+1}{a} = {graph}\n')

export_graphs(graphs64, 'graphs64.txt',64)
export_graphs(graphs32, 'graphs32.txt',32)
export_graphs(graphs16, 'graphs16.txt',16)
export_graphs(graphs8, 'graphs8.txt',8)
export_graphs(graphs4, 'graphs4.txt',4)
export_graphs(graph2, 'graph2.txt',2)


#union all txt files in one txt file

def union_txt_files(filenames, output_filename):
    with open(output_filename, 'w') as outfile:
        for filename in filenames:
            with open(filename) as infile:
                outfile.write(infile.read())

union_txt_files(['graphs64.txt', 'graphs32.txt', 'graphs16.txt', 'graphs8.txt', 'graphs4.txt', 'graph2.txt'], 'graphs.txt')


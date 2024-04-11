import random

def generargrafoconectado(n_nodes, n_graphs):
    graphs = []
    for _ in range(n_graphs):
        graph = {}
        for i in range(n_nodes):
            connections = {}
            for j in range(n_nodes):
                if i != j:
                    # Pesos aleatorios de 1 a 10
                    connections[str(j)] = random.randint(1, 10)
            graph[str(i)] = connections
        graphs.append(graph)
    return graphs

# genera grafos para testeo

graphs64 = generargrafoconectado(64, 5)
graphs32 = generargrafoconectado(32, 5)
graphs16 = generargrafoconectado(16, 5)
graphs8 = generargrafoconectado(8, 5)
graphs4 = generargrafoconectado(4, 5)
graph2 = generargrafoconectado(2, 5)


# exporta los grafos a archivos txt

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


#junta todos los archivos en uno solo

def union_txt_files(filenames, output_filename):
    with open(output_filename, 'w') as outfile:
        for filename in filenames:
            with open(filename) as infile:
                outfile.write(infile.read())

union_txt_files(['graphs64.txt', 'graphs32.txt', 'graphs16.txt', 'graphs8.txt', 'graphs4.txt', 'graph2.txt'], 'graphs.txt')


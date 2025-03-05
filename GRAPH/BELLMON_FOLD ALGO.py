import sys

def bellmanford(graph, src, dest):
    inf = sys.maxsize
    node_data = {
        'A': {'cost': inf, 'pred': []},
        'B': {'cost': inf, 'pred': []},
        'C': {'cost': inf, 'pred': []},
        'D': {'cost': inf, 'pred': []},
        'E': {'cost': inf, 'pred': []},
        'F': {'cost': inf, 'pred': []}
    }
    node_data[src]['cost'] = 0

    # Relax edges |V| - 1 times
    for i in range(len(graph) - 1):
        #print(f'Iteration {i + 1}')
        for temp in graph:
            for neighbor in graph[temp]:
                cost = node_data[temp]['cost'] + graph[temp][neighbor]
                if cost < node_data[neighbor]['cost']:
                    node_data[neighbor]['cost'] = cost
                    node_data[neighbor]['pred'] = node_data[temp]['pred'] + [temp]

        # Display the node_data dictionary after each iteration for debugging purposes
        #print(node_data)

    # Check for negative weight cycles
    for temp in graph:
        for neighbor in graph[temp]:
            cost = node_data[temp]['cost'] + graph[temp][neighbor]
            if cost < node_data[neighbor]['cost']:
                print("Graph contains a negative weight cycle")
                return

    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + [dest]))


if __name__ == "__main__":
    graph = {
        'A': {'B': 6, 'C': 4, 'D': 5},
        'B': {'E': -1},
        'C': {'B': -2, 'E': 3},
        'D': {'C': -2, 'F': -1},
        'E': {'F': 3},
        'F': {}
    }

    source = 'A'
    destination = 'E'
    bellmanford(graph, source, destination)

from heapq import heapify, heappop, heappush


def prims_mst(graph, nodes, start):
    # MST--EDGES
    MST = []

    # VISITED DICTIONARY
    visited = {x: 0 for x in graph}

    # PRIORITY QUEUE
    min_heap = [(0, start, -1)]  # (weight, vertex, parent)

    # WEIGHT--SUM
    weight = 0

    while min_heap:
        w, v, u = heappop(min_heap)

        if u != -1:
            if not visited[v]:
                weight += w
                MST.append((u, v))

        # VISITED MARKING
        visited[v] = 1

        for neighbour in graph[v]:
            if not visited[neighbour]:#this condition to prevent addition of repeated neighbour if is cycled
                heappush(min_heap, (graph[v][neighbour], neighbour, v))

    print(f"MST : {MST}")
    print(f"TOTAL WEIGHT : {weight}")


if __name__ == "__main__":
    graph = {
        0: {1: 4, 7: 8},
        1: {0: 4, 7: 11, 2: 8},
        7: {0: 8, 1: 11, 8: 7, 6: 1},
        2: {1: 8, 8: 2, 3: 7},
        8: {2: 2, 7: 7, 6: 6},
        6: {7: 1, 8: 6, 5: 2},
        3: {2: 7, 5: 14, 4: 9},
        5: {6: 2, 3: 14, 4: 10},
        4: {3: 9, 5: 10}
    }

    prims_mst(graph, len(graph), 0)

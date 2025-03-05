from heapq import heapify,heappush,heappop

def kruskal_mst(graph, n):

    # MST--EDGES
    MST = []

    # VISITED DICTIONARY
    visited = {x: 0 for x in graph}

    # PRIORITY QUEUE
    min_heap = []

    #SORTING ALL EDGES
    for temp in range(1,n+1):
        for j in graph[temp]:
            heappush(min_heap,(graph[temp][j],temp,j))

    # WEIGHT--SUM
    weight = 0

    while min_heap:
        w,v,u = heappop(min_heap)

        if visited[u]==0 or visited[v]==0:
            MST.append((v,u))
            weight += w

        # VISITED MARKING
        visited[v] = visited[u] = 1

    print(f"MST : {MST}")
    print(f"TOTAL WEIGHT : {weight}")


if __name__ == "__main__":
    graph = {
        1: {5: 4, 4: 1, 2: 2},
        2: {1: 2, 4: 3, 3:3, 6:7},
        6: {3: 8, 2: 7},
        3: {4: 5, 2: 3, 6: 8},
        5: {4: 9, 1: 4},
        4: {5: 9, 1: 1,3:5,2:3}
    }

    kruskal_mst(graph, len(graph))
import sys
from heapq import heapify,heappush,heappop

def dijkstra(graph,src,dest):
    inf = sys.maxsize
    node_data ={
        0: {'cost': inf, 'pred': []},
        1: {'cost': inf, 'pred': []},
        2: {'cost': inf, 'pred': []},
        3: {'cost': inf, 'pred': []},
        4: {'cost': inf, 'pred': []},
        5: {'cost': inf, 'pred': []},
        6: {'cost': inf, 'pred': []},
        7: {'cost': inf, 'pred': []},
        8: {'cost': inf, 'pred': []}
    }
    node_data[src]['cost']=0
    visited=[]

    min_heap = [(0,src)] #global priority queue

    while(min_heap):
        heapify(min_heap)
        temp = heappop(min_heap)[1]
        if temp not in visited:
            visited.append(temp)
            for neighbour in graph[temp]:
                if neighbour not in visited:
                    cost = node_data[temp]['cost']+graph[temp][neighbour]
                    if cost < node_data[neighbour]['cost']:
                        node_data[neighbour]['cost'] = cost
                        node_data[neighbour]['pred']=node_data[temp]['pred']+[temp]
                    heappush(min_heap,(node_data[neighbour]['cost'],neighbour))
                    
    print(f"SHORTEST DISTANCE --> {node_data[dest]['cost']}")
    print(f"SHORTEST PATH --> {node_data[dest]['pred']+[dest]}")


if __name__=="__main__":

    graph = {
        0:{1:4,7:8},
        1:{0:4,7:11,2:8},
        7:{0:8,1:11,8:7,6:1},
        2:{1:8,8:2,3:7},
        8:{2:2,7:7,6:6},
        6:{7:1,8:6,5:2},
        3:{2:7,5:14,4:9},
        5:{6:2,3:14,4:10},
        4:{3:9,5:10}
    }

    source = 0
    destination = 3

    dijkstra(graph,source,destination)

# Initialization: The min_heap is initialized with a tuple containing the cost (which is 0 for the source node) and the source node itself. This ensures that the algorithm starts from the source node.
#
# python
# min_heap = [(0, src)]  # (cost, node)
# Heapify: The heapify function is used to maintain the heap property, which ensures that the smallest element is always at the root of the heap. This step is crucial to efficiently find the node with the minimum cost at each iteration.
#
# python
# heapify(min_heap)
# Heap Pop: The heappop function removes and returns the smallest element from the heap, which is the node with the minimum cost to process next. The second element of the tuple (node) is stored in temp.
#
# python
# temp = heappop(min_heap)[1]
# Processing Neighbors: For each neighbor of the current node (temp), the algorithm calculates the cost to reach the neighbor. If this cost is less than the previously known cost, the algorithm updates the cost and the predecessor path in node_data. The neighbor and its updated cost are then pushed into the min_heap.
#
# python
# for neighbour in graph[temp]:
#     if neighbour not in visited:
#         cost = node_data[temp]['cost'] + graph[temp][neighbour]
#         if cost < node_data[neighbour]['cost']:
#             node_data[neighbour]['cost'] = cost
#             node_data[neighbour]['pred'] = node_data[temp]['pred'] + [temp]
#         heappush(min_heap, (node_data[neighbour]['cost'], neighbour))
# Heap Push: The heappush function adds a new element (tuple containing the updated cost and neighbor) to the heap while maintaining the heap property.
#
# python
# heappush(min_heap, (node_data[neighbour]['cost'], neighbour))
# Loop Until Empty: The while loop continues until min_heap is empty, ensuring that all reachable nodes have been processed and the shortest paths have been found.
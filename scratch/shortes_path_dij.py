from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def addEdge(self, u, v, weight):

        new_node = (v, weight)
        self.graph[u].append(new_node)

        new_node = (u, weight)
        self.graph[v].append(new_node)


    def dijkstra(self, u):
        dist = []
        heap = []
        for v in range(self.V):
            if v == u:
                dist.append(0)
                heapq.heappush(heap, (dist[v], v))
            else:
                dist.append(float("inf"))
                heapq.heappush(heap, (dist[v], v))


        while heap:
            new_node = heapq.heappop(heap)
            u = new_node[1]

            for pCrawl in self.graph[u]:

                 v = pCrawl[0]
                 if (dist[v], v) in heap and dist[u] != float('inf') and pCrawl[1] + dist[u] < dist[v]:
                     dist[v] = pCrawl[1] + dist[u]


        return dist


graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)

graph.dijkstra(0)



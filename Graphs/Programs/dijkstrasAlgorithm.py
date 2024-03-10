# Note this algoithm assumes that the src vertex is zero

import sys
class Graph:
    def __init__(self, noOfVertices):
        self.noOfVertices = noOfVertices
        self.adjMatrix = [[0 for i in range(noOfVertices)] for i in range(noOfVertices)]

    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
    
    def removeEdge(self, v1, v2):
        if not self.containsEdge(v1, v2):
            return 
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __getMinVertex(self, dist, visited):
        minVertex = -1
        
        for i in range(self.noOfVertices):
            if((not visited[i]) and (( minVertex == -1) or (dist[minVertex] > dist[i]))):
                minVertex = i

        return minVertex

    def dijkstras(self):
        visited = [False for i in range(self.noOfVertices)]
        dist = [sys.maxsize for i in range(self.noOfVertices)]
        dist[0] = 0

        for i in range(self.noOfVertices -1):
            minVertex = self.__getMinVertex(dist, visited)
            visited[minVertex] = True
            for j in range(self.noOfVertices):
                if not visited[j] and self.containsEdge(minVertex, j):
                    if dist[j] > (dist[minVertex] + self.adjMatrix[minVertex][j]):
                        dist[j] = (dist[minVertex] + self.adjMatrix[minVertex][j])
            
        for i in range(self.noOfVertices):
            print(i, dist[i], sep= " ")
                        

    def __str__(self):
        return str(self.adjMatrix)



nv, ne = map(int, input().split())
g = Graph(nv)
for i in range(ne):
    src, dest, wt = map(int, input().split())
    g.addEdge(src, dest, wt)


g.dijkstras()

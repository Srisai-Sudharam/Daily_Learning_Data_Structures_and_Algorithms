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

    def __getMinVertex(self, weights, visited):
        minVertex = -1
        
        for i in range(self.noOfVertices):
            if((not visited[i]) and (( minVertex == -1) or (weights[minVertex] > weights[i]))):
                minVertex = i
        print(minVertex)
        return minVertex

    def prims(self):
        weights = [sys.maxsize for i in range(self.noOfVertices)]
        parent = [-1 for i in range(self.noOfVertices)]
        visited = [False for i in range(self.noOfVertices)]
        weights[0] = 0
        for i in range(self.noOfVertices -1):
            #pick a vertex part
       

            minVertex = self.__getMinVertex(weights, visited)
            visited[minVertex] = True

            

            #explore neighbours and update weights and parent array
            for j in range(self.noOfVertices):
                if not visited[i] and self.containsEdge(minVertex, j):
                    if(weights[j] > self.adjMatrix[minVertex][j]):
                        weights[j] = self.adjMatrix[minVertex][j]
                        parent[j] = minVertex
        
        for i in range(1, self.noOfVertices):

            if(i < parent[i] ):
                print(i, parent[i], weights[i], sep=" ")
            else:
                print(parent[i], i, weights[i], sep=" ")

    def __str__(self):
        return str(self.adjMatrix)



nv, ne = map(int, input().split())
g = Graph(nv)
for i in range(nv):
    src, dest, wt = map(int, input().split())
    g.addEdge(src, dest, wt)

print(g)
g.prims()

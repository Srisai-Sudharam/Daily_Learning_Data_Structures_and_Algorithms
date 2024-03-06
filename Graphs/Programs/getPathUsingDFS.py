class Graph:
    def __init__(self, noOfVertices):
        self.noOfVertices = noOfVertices
        self.adjMatrix = [[0 for i in range(noOfVertices)] for i in range(noOfVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self, v1, v2):
        if not self.containsEdge(v1, v2):
            return 
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        return str(self.adjMatrix)

    def __getPathHelper(self, sv, ev, visitedVertices):
        visitedVertices[sv] = True
        if self.adjMatrix[sv][ev] == 1:
            return [ev, sv]
        
        for i in range(self.noOfVertices):
            if not visitedVertices[i] and self.adjMatrix[sv][i] == 1:
                path = self.__getPathHelper(i, ev, visitedVertices)
                if path is not None:
                    path.append(sv)
                    
                    return path
            
        return None


    def getPathDFS(self, v1, v2):
        visitedVertices = [False for i in range(self.noOfVertices)]
        return self.__getPathHelper(v1, v2, visitedVertices)

g = Graph(4)

g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(2, 3)


print(g.getPathDFS(1, 3))
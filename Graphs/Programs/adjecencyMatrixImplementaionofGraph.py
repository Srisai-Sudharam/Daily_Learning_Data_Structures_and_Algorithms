class Graph: 
    def __init__(self, noOfVertices):
        self.noOfVertices = noOfVertices
        self.adjMatrix =  [[0 for i in range(noOfVertices) ] for j in range(noOfVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self, v1, v2):
        if self.containsEdge(v2, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __dfsHelper(self, startingVertex, visitedVertices):
        print(startingVertex)
        visitedVertices[startingVertex] = True
        for i in range(self.noOfVertices):
            if self.adjMatrix[startingVertex][i]>0 and visitedVertices[i] is False:
                self.__dfsHelper(i, visitedVertices)
        

    def dfs(self):
        visitedVertices = [False for i in range(self.noOfVertices) ]
        self.__dfsHelper(0, visitedVertices)
    
    def __str__(self):
        return str(self.adjMatrix)

    


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(2, 4)

g.dfs()
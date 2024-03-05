import queue

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
        

    def dfs(self): #dfs corrected
        visitedVertices = [False for i in range(self.noOfVertices) ]
        for i in range(self.noOfVertices):
            if not visitedVertices[i]:
                self.__dfsHelper(i, visitedVertices)
    

    def __bfsHelper(self, sv, visitedVertices):
        q = queue.Queue()
        q.put(sv)
        visitedVertices[sv] = True
        while(not q.empty()):
            vertex = q.get()
            print(vertex)

            for i in range(self.noOfVertices):
                if not visitedVertices[i] and self.containsEdge(vertex, i):
                    q.put(i)
                    visitedVertices[i] = True # it is better to mark node as visited here there can be duplicate nodes inserted in queue in case of cycle in graph


    def bfs(self):
        visitedVertices = [False for i in range(self.noOfVertices)]
        for i in range(self.noOfVertices):
            if not visitedVertices[i]:
                self.__bfsHelper(i, visitedVertices)

            
    def __hasPathHelper(self, v1, v2, visitedVertices):
        visitedVertices[v1] = True
        if self.adjMatrix[v1][v2] > 0:
            return True
        result = False
        for i in range(self.noOfVertices):
            if not visitedVertices[i] and self.adjMatrix[v1][i] > 0:
                result = result or self.__hasPathHelper(i, v2, visitedVertices)
        return result
    
    def has_path(self, v1, v2):
        visitedVertices = [False for i in range(self.noOfVertices)]
        return self.__hasPathHelper(v1, v2, visitedVertices)


    def hasPathUsingBFS(self, sv, ev):
        if sv == ev:
            return True
        
        visitedVertices = [False for i in range(self.noOfVertices)]
        q = queue.Queue()
        q.put(sv)
        visitedVertices[sv] = True

        while( not q.empty()):
            vertex = q.get()
            
            for i in range(self.noOfVertices):
                if self.containsEdge(vertex, i) and not visitedVertices[i]:
                    if i == ev:
                        return True
                    q.put(i)
                    visitedVertices[i] = True
        return False

    def __str__(self):
        return str(self.adjMatrix)

    


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(3, 4)


print(g.has_path(0, 2))
print(g.hasPathUsingBFS(0, 2))


g.bfs()
import queue

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
    
    def __isConnected(self, sv, visited):
        
        visited[sv] = True

        for i in range(self.noOfVertices):
            if not visited[i] and self.containsEdge(sv, i):
                print(sv, i)
                self.__isConnected(i, visited)
    


    def isConnected(self):
        visited = [False for i in range(self.noOfVertices)]
        self.__isConnected(0, visited)
        answer = True
        for i in visited:
            answer = answer and i
        return answer


    


        

g = Graph(5)

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)



print(g.isConnected())
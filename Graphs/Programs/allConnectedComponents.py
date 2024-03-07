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
    
    def __allConnectedComponentsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        path = []

        while(not q.empty()):
            front = q.get()
            path.append(front)
            for i in range(self.noOfVertices):
                if not visited[i] and self.containsEdge(front, i):
                    q.put(i)
                    visited[i] = True
        return path

    
    def allConnectedComponents(self):
        paths = []
        visited = [False for i in range(self.noOfVertices)]
        for i in range(self.noOfVertices):
            if not visited[i]:
                paths.append(self.__allConnectedComponentsHelper(i, visited))
        return paths

g = Graph(6)

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 2)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(3, 5)


print(g.allConnectedComponents())
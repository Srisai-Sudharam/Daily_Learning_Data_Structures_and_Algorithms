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
    
    def __getPathBFS(self, sv, ev, visited):
        if self.containsEdge(sv, ev) or sv == ev:
            return [sv]
        
        mapp = {}
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        mapp[sv] = None

        while(not q.empty()):
            front = q.get()

            for i in range(self.noOfVertices):
                if not visited[i] and self.containsEdge(front, i):
                    mapp[i] = front   
                    q.put(i)
                    visited[i] = True

                    if i == ev:
                        path = []
                        path.append(ev)
                        value = ev
                        while(mapp[value] is not None):
                            value = mapp[value]
                            path.append(value)
                        return path
        return []
                        
                            



    
    def getPathBFS(self, sv, ev):
        if(sv < 0 or ev > self.noOfVertices - 1):
            return []
        visited = [False for i in range(self.noOfVertices)]

        return self.__getPathBFS(sv, ev, visited)


        

g = Graph(6)

g.addEdge(5, 3)
g.addEdge(0, 1)
g.addEdge(3, 4)





print(g.getPathBFS(0, 3))
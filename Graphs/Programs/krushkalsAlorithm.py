# A Spanning tree is a tree that can be derived from graph
# since a tree does not have cycle and isconnected it will have n vertices and n-1 edges
# there can be so many spanning trees possible for a graph, the on with minimum weight is considered as minimum spanning tree
# Kruskal algorithm is used to find that spanning tree


#below we are using kruskal algorithm with union and find algorithm

#step - 1: Take input and store graph (here we are using edgeList approach since kruskals algorithms works based on edges order)
#step - 2: sort the edges in order of their weights
#step - 3: count = 0, create parent array
#   while(count <= noOfVertices -1)
#   currentEdge = edgeList(i)
#   if parentOfVertex1 != parentOfVertex2
#   append edge to minimum spanning tree and update parent array
# return the minumum spanning tree


class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest 
        self.wt = wt
 


def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)



def kruskalsAlgorithm(edgeList, noOfVertices):
    sortedEdgeList = sorted(edgeList, key= lambda edge: edge.wt )
    count = 0
    parent = [i for i in range(noOfVertices)]
    minimumSpanningTree = []
    i = 0
    while(count <= noOfVertices - 1 and i < noOfVertices):
        currentEdge = sortedEdgeList[i]
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dest, parent)
        

        if srcParent != destParent:
            minimumSpanningTree.append(currentEdge)
            parent[srcParent] = destParent
            count+=1
        i+=1

    return minimumSpanningTree


def printEdgeList(edgeList):
    for i in edgeList:
        if i.src < i.dest:
            print(i.src, i.dest, i.wt, sep=" ")
        else:
            print(i.dest, i.src, i.wt, sep=" ")


edgeList = []    
li = [int(ele) for ele in input().split()]
n, e = li
for i in range(e):
    src, dest, wt = input().split()
    edge = Edge(int(src), int(dest), int(wt))
    edgeList.append(edge)



mst = kruskalsAlgorithm(edgeList, n)
print("---------")
printEdgeList(mst)
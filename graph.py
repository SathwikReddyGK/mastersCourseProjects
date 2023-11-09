# Graph class if possible
# class Vertex:
#     def __init__(self,vertex):
#         self.id = vertex
#         self.vertexNeighbours = {}
# class Graph:
#     # Constructor
#     def __init__(self,n):
#         # # create a adjacency list to hold vertices, edges and weight
#         # self.graphAdjList = []

#         # create a list to hold all the vertices objects
#         self.verticesList = []

#         # load the vertices list will all the vertices and objects
#         # and add empty 
#         for i in range(1,n+1):
#             self.createVertices(i)

    
#     def createVertices(self,vertex):
#         self.verticesList.append(Vertex(vertex))

import random
from queue import Queue

def breadthFirstSearch(n,graph):
    
    # BFS for specific vertex
    def bfsForVertex(vertex):
        # Queue to hold vertices to be visited
        vertQueue = Queue(n)

        for col in range(0,n):
            if graph[vertex][col] > 0 and graph[vertex][col] not in verticesPathDistance[]:
                verticesPathDistance[graph[vertex][col]] = 1
                vertQueue.put(col)


    # Dictionary to hold distance of vertices
    verticesPathDistance = {}


    


def djikstrasShortestPath(n,graph):
    def relaxation(vertex):
        if len(unvisitedVertices) <= 0:
            return
        if vertex in visitedVertices:
            return
        unvisitedVertices.pop(vertex)
        visitedVertices.append(vertex)
        for i in range(0,n):
            if vertex != i and graph[vertex][i] > 0 and verticesPathDistance[i] > (verticesPathDistance[vertex] + graph[vertex][i]):
                verticesPathDistance[i] = verticesPathDistance[vertex] + graph[vertex][i]
        
        minVertex = 0
        for i in range(0,n):
            if vertex != i and graph[vertex][i] > 0:
                if minVertex > verticesPathDistance[i]:
                    minVertex = i
        
        relaxation(minVertex)

    # Printing graph just to use it to do testing
    print(graph)

    # Dictionary to hold distance of vertices
    verticesPathDistance = {}
    # List to maintain unvisited vertices
    unvisitedVertices = []
    # List to maintain visited vertices
    visitedVertices = []
    
    # Considering 0 as the source node, so assiging distance as 0 and rest of the vertices will be
    # assigned float(inf) to represent it as infinity
    # Also update unvisitedVertices list with all the vertices
    verticesPathDistance[0] = 0
    unvisitedVertices.append(0)
    for i in range(1,n):
        verticesPathDistance[i] = float('inf')
        unvisitedVertices.append(i)
    
    # Begin relaxation of all vertices
    relaxation(0)

    # To test the algorithm
    print(verticesPathDistance)

    
    

        


if __name__ == "__main__":
    # Take input from user
    n = int(input("Please enter the number of vertices: "))
    # Build 2d Array for Weighted Graph
    graph = [ [random.randrange(1,20) for i in range(0,n)] for j in range(0,n)]
    djikstrasShortestPath(n,graph)


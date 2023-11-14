import random
import time
import matplotlib.pyplot as algoplot
import networkx as genGraph
from queue import Queue
from collections import defaultdict

def createGraph(n):
    graph = genGraph.complete_graph(n)
    graph2D = [[0 for _ in range(n)] for _ in range(n)]
    for edge in graph.edges():
        graph[edge[0]][edge[1]]['weight'] = random.randrange(1,20)
    
    for row in range(0,n):
        for col in graph.adj[row]:
            graph2D[row][col] = graph.adj[row][col]['weight']

    return graph2D

def plotComparisionSameInputSize(n,shortestPathAlgos,timeTaken):
    algoplot.plot(shortestPathAlgos,timeTaken,marker='o')
    algoplot.xlabel('Shortest Path Algorithms')
    algoplot.ylabel('Time Taken in milli seconds')
    title = 'Comparision of time taken between shortest path algorithms for ' + str(n) + ' Vertices.'
    algoplot.title(title)
    algoplot.show()

def plotForDifferentInputSizes(inputSizes,algorithm,timeTaken):
    algoplot.plot(inputSizes,timeTaken,marker='o')
    algoplot.xlabel('Input Sizes')
    algoplot.ylabel('Time Taken in milli seconds')
    title = 'Comparision of time taken by ' + algorithm + ' for different input sizes.'
    algoplot.title(title)
    algoplot.show()

def prepareOut(graph):
    # Printing graph just to use it to do testing
    print("\n")
    print("Generated Graph:")
    print(graph)
    print("\n")

def bfsTiming(n,graph,sourceVertex):
    print("Breadth First Search: ")
    bfsStartTime = time.monotonic_ns()
    breadthFirstSearch(n,graph,sourceVertex)
    bfsEndTime = time.monotonic_ns()
    timeTaken = (bfsEndTime-bfsStartTime)/1000000
    print(type(timeTaken))
    print("Time taken in seconds to find the distance of all other nodes from source node: ", timeTaken)
    return timeTaken

def djikstraTiming(n,graph,sourceVertex):
    print("Djikstra: ")
    djikstraStartTime = time.monotonic_ns()
    djikstrasShortestPath(n,graph,sourceVertex)
    djikstraEndTime = time.monotonic_ns()
    timeTaken = (djikstraEndTime-djikstraStartTime)/1000000
    print("Time taken in seconds to find the distance of all other nodes from source node: ", timeTaken)
    return timeTaken

def bellmanFordTiming(n,graph,sourceVertex):
    print("Bellman Ford: ")
    bellmanFordStartTime = time.monotonic_ns()
    bellmanFordAlgo(n,graph,sourceVertex)
    bellmanFordEndTime = time.monotonic_ns()
    timeTaken = (bellmanFordEndTime-bellmanFordStartTime)/1000000
    print("Time taken in seconds to find the distance of all other nodes from source node: ", timeTaken)
    return timeTaken

def bellmanFordAlgo(n,graph,sourceVertex):

    # Relax all the edges
    def relaxEdges(n,graph,negativeCycleCheck):
        for source in range(0,n):
            for dest in range(0,n):
                if dest != source and graph[source][dest] != 0 and verticesDistanceDict[dest]>(verticesDistanceDict[source] + graph[source][dest]):
                    if negativeCycleCheck == True:
                        return True
                    verticesDistanceDict[dest] = verticesDistanceDict[source] + graph[source][dest]

    # Dictionary to hold the list of vertices and their distances
    verticesDistanceDict = {}

    # Build the dictionary with weight as 0 for source vertex and inf for all other vertices
    verticesDistanceDict[sourceVertex] = 0
    for i in range(0,n):
        if i == sourceVertex:
            continue
        verticesDistanceDict[i] = float('inf')
    
    # Relax the edges V-1 times, V-Vertices
    counter = 1
    while counter < n:
        relaxEdges(n,graph,False)
        counter += 1
    
    # Check if there exits a negative cycle
    hasNegativeCycle = relaxEdges(n,graph,True)
    if hasNegativeCycle == True:
        print("Cannot determine shortest path, negative cycle exists")
    
    # Print the shortest paths to output for testing
    print(verticesDistanceDict)


# Breadth First Search Algorithm to find the shortest path
def breadthFirstSearch(n,graph,sourceVertex):
    
    # BFS for specific vertex
    def bfsForVertex(vertex):

        for col in range(0,n):
            if col != vertex and graph[vertex][col] != 0 and col not in verticesPathDistance:
                verticesPathDistance[col] = verticesPathDistance[vertex] + 1
                vertQueue.put(col)
            elif col == vertex and col not in verticesPathDistance:
                verticesPathDistance[col] = 0
    
    def relaxQueue():
        while not(vertQueue.empty()):
            tempVertex = vertQueue.get()
            bfsForVertex(tempVertex)
            


    # Queue to hold vertices to be visited
    vertQueue = Queue(n)

    # Dictionary to hold distance of vertices
    verticesPathDistance = defaultdict(lambda: 0)

    # For Vertex 0 check the shortest path for vertices connected and add connected vertices to queue
    bfsForVertex(sourceVertex)
    
    # Working with all the vertices which were connected to vertex 0 and continuing with BFS
    relaxQueue()

    # Printing the vertices and distance for testing
    print(verticesPathDistance.items())


def djikstrasShortestPath(n,graph,sourceVertex):
    # Relaxation of all the vertices
    def relaxation(vertex):
        if len(unvisitedVertices) <= 0:
            return
        if vertex in visitedVertices:
            return
        unvisitedVertices.remove(vertex)
        visitedVertices.append(vertex)
        for i in range(0,n):
            if vertex != i and graph[vertex][i] > 0 and verticesPathDistance[i] > (verticesPathDistance[vertex] + graph[vertex][i]):
                verticesPathDistance[i] = verticesPathDistance[vertex] + graph[vertex][i]
        
        minVertex = 0
        minDistance = float('inf')
        for i in range(0,n):
            if vertex != i and graph[vertex][i] > 0:
                if minDistance > verticesPathDistance[i]:
                    minVertex = i
                    minDistance = verticesPathDistance[i]
        
        relaxation(minVertex)

    # Dictionary to hold distance of vertices
    verticesPathDistance = {}
    # List to maintain unvisited vertices
    unvisitedVertices = []
    # List to maintain visited vertices
    visitedVertices = []
    
    # Considering 0 as the source node, so assiging distance as 0 and rest of the vertices will be
    # assigned float(inf) to represent it as infinity. Keeping list of all possible vertices
    # Also update unvisitedVertices list with all the vertices
    verticesPathDistance[sourceVertex] = 0
    unvisitedVertices.append(sourceVertex)
    for i in range(0,n):
        if i == sourceVertex:
            continue
        verticesPathDistance[i] = float('inf')
        unvisitedVertices.append(i)
    
    # Begin relaxation of all vertices
    relaxation(sourceVertex)

    # To test the algorithm
    # print(verticesPathDistance)

def handleCompare(algorithm,xaxis,yaxis,n,graph,sourceVertex):
    if algorithm == "Breadth For Search":
        yaxis.append(bfsTiming(n,graph,sourceVertex))
        xaxis.append('BFS')
    elif algorithm == "Bellman Ford":
        yaxis.append(bellmanFordTiming(n,graph,sourceVertex))
        xaxis.append('Bellman Ford')
    elif algorithm == "Dijkstra":
        yaxis.append(djikstraTiming(n,graph,sourceVertex))
        xaxis.append('Djikstra')

def main(n,sourceVertex,algorithm,compare,algorithm1,algorithm2,algorithm3):

    # Take input from user
    # n = int(input("Please enter the number of vertices: "))

    # Taking source vertex as input
    # sourceVertex = int(input("Please enter the source vertex: "))

    # Build 2d Array for Weighted Graph, a 2D array generated
    # graph = [ [random.randrange(1,20) for i in range(0,n)] for j in range(0,n)]

    # Check if user wants to compare or run individually
    # compare = input("Please enter C-To compare between algorithms, I-To run individual algorithms, A-To run all algorithms")
    # compare = compare.upper()

    # Djikstra/BFS Test Case
    # graph = [[0,2,4,0,0,0],[0,0,1,7,0,0],[0,0,0,0,3,0],[0,0,0,0,0,1],[0,0,0,2,0,5],[0,0,0,0,0,0]]

    # Bellman/BFS Ford Test Case
    # graph = [[0,6,5,5,0,0,0],[0,0,0,0,-1,0,0],[0,-2,0,0,1,0,0],[0,0,-2,0,0,-1,0],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,0]]

    if compare == True:
        # Run algorithms and print their timing based on user selection
        # Generated using python library graph function
        graph = createGraph(n)
        prepareOut(graph)
        xaxis = []
        yaxis = []
        handleCompare(algorithm1,xaxis,yaxis,n,graph,sourceVertex)
        handleCompare(algorithm2,xaxis,yaxis,n,graph,sourceVertex)
        handleCompare(algorithm3,xaxis,yaxis,n,graph,sourceVertex)
        plotComparisionSameInputSize(n,xaxis,yaxis)

    else:
        # prepareOut(graph)
        xaxis = []
        yaxis = []
        for inSize in range(150,500,10):
            xaxis.append(inSize)
            # graph = [ [random.randrange(1,20) for i in range(0,inSize)] for j in range(0,inSize)]
            graph = createGraph(inSize)
            if algorithm == "B":
                yaxis.append(bfsTiming(inSize,graph,sourceVertex))
                algoTitle = 'BFS'
            elif algorithm == "D":
                yaxis.append(djikstraTiming(inSize,graph,sourceVertex))
                algoTitle = 'Djikstra'
            elif algorithm == "F":
                yaxis.append(bellmanFordTiming(inSize,graph,sourceVertex))
                algoTitle = 'Bellman Form'

        plotForDifferentInputSizes(xaxis,algoTitle,yaxis)

    if compare == 'C':
        # prepareOut(graph)
        pass
    elif compare == 'I':
        # Taking the algorithm to be selected by user
        algorithm = input("Please enter B-BFS, D-Djikstra , F-Bellman Ford: ")
        algorithm = algorithm.upper()

        # prepareOut(graph)
        xaxis = []
        yaxis = []
        for inSize in range(150,500,10):
            xaxis.append(inSize)
            # graph = [ [random.randrange(1,20) for i in range(0,inSize)] for j in range(0,inSize)]
            graph = createGraph(inSize)
            if algorithm == "B":
                yaxis.append(bfsTiming(inSize,graph,sourceVertex))
                algoTitle = 'BFS'
            elif algorithm == "D":
                yaxis.append(djikstraTiming(inSize,graph,sourceVertex))
                algoTitle = 'Djikstra'
            elif algorithm == "F":
                yaxis.append(bellmanFordTiming(inSize,graph,sourceVertex))
                algoTitle = 'Bellman Form'

        plotForDifferentInputSizes(xaxis,algoTitle,yaxis)

    elif compare == 'A':
        # Run all algorithms and print their timing
        prepareOut(graph)
        yaxis = [bfsTiming(n,graph,sourceVertex),djikstraTiming(n,graph,sourceVertex),bellmanFordTiming(n,graph,sourceVertex)]
        xaxis = ['BFS','Djikstra','Bellman Ford']
        plotComparisionSameInputSize(n,xaxis,yaxis)

# if __name__ == "__main__":
#     main()

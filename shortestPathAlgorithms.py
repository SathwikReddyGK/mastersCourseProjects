import random
import time
import matplotlib.pyplot as algoplot
import networkx as genGraph
from queue import Queue
from collections import defaultdict

# Fucntion Generating Graph using networkx Library to be used to run and test the algorithms
def createGraph(n):
    # Using Complete Graph from networkx to generate a graph of n vertices
    graph = genGraph.complete_graph(n)

    graph2D = [[0 for _ in range(n)] for _ in range(n)]

    # Update weight for the graph edges randomly generated between 1 and 20
    for edge in graph.edges():
        graph[edge[0]][edge[1]]['weight'] = random.randrange(1,20)
    
    # Generate a 2D matrix from the generated graph
    for row in range(0,n):
        for col in graph.adj[row]:
            graph2D[row][col] = graph.adj[row][col]['weight']

    count = n//2
    while(count > 0):
        count -= 1
        row = random.randrange(1,n)
        col = random.randrange(1,n)
        graph2D[row][col] = 0

    # return the generated 2D Matrix of Graph and it's weight
    return graph2D

# Generate Plot for an input size against time taken by multiple algorithms, comparing performance between algorithms
def plotComparisionSameInputSize(n,shortestPathAlgos,timeTaken):
    algoplot.plot(shortestPathAlgos,timeTaken,marker='x')
    algoplot.xlabel('Shortest Path Algorithms')
    algoplot.ylabel('Time Taken in milli seconds')
    title = 'Comparision of time taken between shortest path algorithms for ' + str(n) + ' Vertices.'
    algoplot.title(title)
    algoplot.show()

# Generate Plot for multiple input sizes with time taken for each size by an algorithm
def plotForDifferentInputSizes(inputSizes,algorithm,timeTaken):
    algoplot.plot(inputSizes,timeTaken,marker='x')
    algoplot.xlabel('Input Sizes')
    algoplot.ylabel('Time Taken in milli seconds')
    title = 'Comparision of time taken by ' + algorithm + ' for different input sizes.'
    algoplot.title(title)
    algoplot.show()

# Generate Plot for an input size against time taken by an algorithm, it would just be a point
# on a graph, using graph instead of printing
def plotForInputSize(inputSize,algorithm,timeTaken):
    algoplot.plot(inputSize,timeTaken,marker='x')
    algoplot.xlabel('Input Size')
    algoplot.ylabel('Time Taken in milli seconds')
    title = 'Time taken by ' + algorithm + ' for input size ' + str(inputSize[0]) + '.'
    algoplot.title(title)
    algoplot.show()

# Printing graph just to use it to do testing
def prepareOut(graph):
    print("\n")
    print("Generated Graph:")
    print(graph)
    print("\n")

# Function to check the time taken by BFS algorithm to find shortest path of all vertices from
# source vertex
def bfsTiming(n,graph,sourceVertex):
    print("Breadth First Search: ")
    bfsStartTime = time.monotonic_ns()
    breadthFirstSearch(n,graph,sourceVertex)
    bfsEndTime = time.monotonic_ns()
    timeTaken = (bfsEndTime-bfsStartTime)/1000000
    print(type(timeTaken))
    print("Time taken in milli seconds to find the distance of all other nodes from source node: ", timeTaken)
    return timeTaken

# Function to check the time taken by Djikstra algorithm to find shortest path of all vertices from
# source vertex
def djikstraTiming(n,graph,sourceVertex):
    print("Djikstra: ")
    djikstraStartTime = time.monotonic_ns()
    djikstrasShortestPath(n,graph,sourceVertex)
    djikstraEndTime = time.monotonic_ns()
    timeTaken = (djikstraEndTime-djikstraStartTime)/1000000
    print("Time taken in milli seconds to find the distance of all other nodes from source node: ", timeTaken)
    return timeTaken

# Function to check the time taken by Bellman Ford algorithm to find shortest path of all vertices from
# source vertex
def bellmanFordTiming(n,graph,sourceVertex):
    print("Bellman Ford: ")
    bellmanFordStartTime = time.monotonic_ns()
    bellmanFordAlgo(n,graph,sourceVertex)
    bellmanFordEndTime = time.monotonic_ns()
    timeTaken = (bellmanFordEndTime-bellmanFordStartTime)/1000000
    print("Time taken in milli seconds to find the distance of all other nodes from source node: ", timeTaken)
    return timeTaken

# Bellman Ford Algorithm to find the shortest path
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
    # print(verticesDistanceDict)


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

    # For Vertex sourceVertex check the shortest path for vertices connected and add connected vertices to queue
    bfsForVertex(sourceVertex)
    
    # Working with all the vertices which were connected to vertex 0 and continuing with BFS
    relaxQueue()

    # Printing the vertices and distance for testing
    # print(verticesPathDistance.items())

# Djikstra Algorithm to find the shortest path
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
    
    # Considering sourceVertex as the source node, so assiging distance as 0 and rest of the vertices will be
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

    # Printing the vertices and distance for testing
    # print(verticesPathDistance.items())

# When Compare Checkbox is selected on GUI, algorithms whose run time needs to be compared will be
# passed, based on that, running the algorithms and updating the time taken and xaxis name to be
# considered on plot
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

# When running one algorithm for a specific input size, running that algorithm and displaying
# the plot which shows the runtime for that algorithm
def handleSinglerun(algorithm,xaxis,yaxis,n,graph,sourceVertex):
    xaxis.append(n)
    if algorithm == "Breadth For Search":
        yaxis.append(bfsTiming(n,graph,sourceVertex))
    elif algorithm == "Bellman Ford":
        yaxis.append(bellmanFordTiming(n,graph,sourceVertex))
    elif algorithm == "Dijkstra":
        yaxis.append(djikstraTiming(n,graph,sourceVertex))

# When running one algorithm for a input range, running that algorithm and displaying
# the plot which shows the runtimes for that algorithm against multiple ranges
def inputSizeRange(algorithm,sourceVertex,rangeLow,rangeHigh,rangeStep,xaxis,yaxis):
    for inSize in range(rangeLow,rangeHigh+1,rangeStep):
        xaxis.append(inSize)
        graph = createGraph(inSize)
        prepareOut(graph)
        if algorithm == "Breadth For Search":
            yaxis.append(bfsTiming(inSize,graph,sourceVertex))
        elif algorithm == "Dijkstra":
            yaxis.append(djikstraTiming(inSize,graph,sourceVertex))
        elif algorithm == "Bellman Ford":
            yaxis.append(bellmanFordTiming(inSize,graph,sourceVertex))

def main(n,sourceVertex,algorithm,compare,algorithm1,algorithm2,algorithm3,rangeLow,rangeHigh,rangeStep,rangeCheckBox):
    # Build 2d Array for Weighted Graph, a 2D array generated, initial 2D array logic
    # graph = [ [random.randrange(1,20) for i in range(0,n)] for j in range(0,n)]

    # Djikstra/BFS Test Case
    # graph = [[0,2,4,0,0,0],[0,0,1,7,0,0],[0,0,0,0,3,0],[0,0,0,0,0,1],[0,0,0,2,0,5],[0,0,0,0,0,0]]

    # Bellman/BFS Ford Test Case
    # graph = [[0,6,5,5,0,0,0],[0,0,0,0,-1,0,0],[0,-2,0,0,1,0,0],[0,0,-2,0,0,-1,0],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,0]]

    if compare == True:
        # Generate Graph for input size provided
        graph = createGraph(n)
        # Printing graph in output for reference
        prepareOut(graph)

        # Initialize xaxis and yaxis
        xaxis = []
        yaxis = []
        # Running for each algorithms passed
        handleCompare(algorithm1,xaxis,yaxis,n,graph,sourceVertex)
        handleCompare(algorithm2,xaxis,yaxis,n,graph,sourceVertex)
        handleCompare(algorithm3,xaxis,yaxis,n,graph,sourceVertex)
        # Plot the comparision
        plotComparisionSameInputSize(n,xaxis,yaxis)

    elif rangeCheckBox == False:
        # Initialize xaxis and yaxis
        xaxis = []
        yaxis = []

        # Generate Graph for input size provided
        graph = createGraph(n)

        # Printing graph in output for reference
        prepareOut(graph)

        # Run the algorithm to get the time taken for input size
        handleSinglerun(algorithm,xaxis,yaxis,n,graph,sourceVertex)

        # Plot the output
        plotForInputSize(xaxis,algorithm,yaxis)
    elif rangeCheckBox == True:
        # Initialize xaxis and yaxis
        xaxis = []
        yaxis = []

        # Run the algorithm to get the time taken for range of input sizes
        inputSizeRange(algorithm,sourceVertex,rangeLow,rangeHigh,rangeStep,xaxis,yaxis)

        # Plot the graph for different input sizes against run time taken by an algorithm
        plotForDifferentInputSizes(xaxis,algorithm,yaxis)

from GraphDependencies.DSALinkedLists import DSALinkedList
from GraphDependencies.DSAqueues import DSALinkedListQueue
from GraphDependencies.DSAstack import DSALinkedListStack

class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()  # Create an instance of DSALinkedList for vertices
        self.edges = DSALinkedList()     # Create an instance of DSALinkedList for edges

    class DSAGraphVertex():
        def __init__(self, label, value):
            self.label = label
            self.value = value
            self.visited = False
            self.visitedInCurrentTraversal = False
            self.adjacentVertices = DSALinkedList()  # Create an instance of DSALinkedList for adjacent vertices
            self.adjacentEdges = DSALinkedList() # Create an instance of DSALinkedList for adjacent edges

        def getLabel(self):
            return self.label

        def getValue(self):
            return self.value

        def setVisited(self):
            self.visited = True

        def clearVisited(self):
            self.visited = False

        def getVisited(self):
            return self.visited

        def addAdjacentVertex(self, vertex):
            self.adjacentVertices.insertLast(vertex)

        def getAdjacentVertex(self):
            return self.adjacentVertices
        
        def addAdjacentEdge(self, edge):
            self.adjacentEdges.insertLast(edge)

        def getAdjacentEdge(self):
            return self.adjacentEdges

        def __str__(self):
            return f"Label: {self.label}\tValue: {self.value}"

    class DSAGraphEdge():
        def __init__(self, origin, destination, label, value) -> None:
            self.origin = origin
            self.destination = destination
            self.label = label
            self.value = value

        def getLabel(self):
            return self.label
        
        def getValue(self):
            return self.value

        def getOrigin(self):
            return self.origin
        
        def getDestination(self):
            return self.destination
        
        def __str__(self):
            return f"Label: {self.label}\tValue: {self.value}\tOrigin: {self.origin}\tDestination: {self.destination}"

    def addVertex(self, label, value) -> None:
        vertex = self.DSAGraphVertex(label, value)
        self.vertices.insertLast(vertex)

    def addEdge(self, origin, destination, label, value) -> None:
        # Check if the origin and destination vertices exist
        if not self.hasVertex(origin) or not self.hasVertex(destination):
            raise ValueError("Origin or destination vertex does not exist")

        # Create the edge
        edge = self.DSAGraphEdge(origin, destination, label, value)
        self.edges.insertLast(edge)

        # Update the adjacency information for the vertices
        originVertex = self.getVertex(origin)
        destinationVertex = self.getVertex(destination)

        originVertex.addAdjacentVertex(destinationVertex)
        destinationVertex.addAdjacentVertex(originVertex)
        originVertex.addAdjacentEdge(edge)
        destinationVertex.addAdjacentEdge(edge)


    def hasVertex(self, label):
        # Check if a vertex with the given label exists in the graph
        currentVertex = self.vertices.head
        while currentVertex is not None:
            if currentVertex.getValue().getLabel() == label:
                return True
            currentVertex = currentVertex.getNext()
        return False

    def getVertexCount(self) -> int:
        # Return the number of vertices in the graph
        return self.vertices.size()

    def getEdgeCount(self) -> int:
        # Return the number of edges in the graph
        return self.edges.size()

    def getVertex(self, label):
        # Return the vertex with the given label
        currentVertex = self.vertices.head
        while currentVertex is not None:
            if currentVertex.getValue().getLabel() == label:
                return currentVertex.getValue()
            currentVertex = currentVertex.getNext()
        return None

    def getEdge(self, origin, destination):
        # Return the edge with the given labels
        currentEdge = self.edges.head
        while currentEdge is not None:
            edge = currentEdge.getValue()
            if (edge.getOrigin() == origin and edge.getDestination() == destination) or \
            (edge.getOrigin() == destination and edge.getDestination() == origin):
                return edge
            currentEdge = currentEdge.getNext()
        return None

    def getAdjacentVertices(self, label):
        # Return a list of adjacent vertices for the vertex with the given label
        vertex = self.getVertex(label)
        vertices = DSALinkedList()
        if vertex:
            for v in vertex.getAdjacentVertex():
                vertices.insertLast(v.getLabel())
        return vertices

    def getAdjacentEdges(self, label):
        # Return a list of adjacent edges for the vertex with the given label
        adjacentEdges = DSALinkedList()
        currentEdge = self.edges.head
        while currentEdge is not None:
            edge = currentEdge.getValue()
            if edge.getOrigin() == label or edge.getDestination() == label:
                adjacentEdges.insertLast(edge)
            currentEdge = currentEdge.getNext()
        return adjacentEdges
    
    def deleteVertex(self, label):
        # Check if the vertex exists
        if not self.hasVertex(label):
            raise ValueError("Vertex does not exist")

        # Get the vertex to be deleted
        vertexToDelete = self.getVertex(label)

        # Remove all edges connected to the vertex
        for edge in list(vertexToDelete.getAdjacentEdge()):
            self.deleteEdge(edge.getOrigin(), edge.getDestination())

        # Remove the vertex from the list of vertices
        self.vertices.remove(vertexToDelete)

    def deleteEdge(self, origin, destination):
        # Check if both origin and destination vertices exist
        if not self.hasVertex(origin) or not self.hasVertex(destination):
            raise ValueError("Origin or destination vertex does not exist")

        # Find the edge to be deleted
        edgeToDelete = None
        for edge in self.edges:
            if (edge.getOrigin() == origin and edge.getDestination() == destination) or \
            (edge.getOrigin() == destination and edge.getDestination() == origin):
                edgeToDelete = edge
                break

        if edgeToDelete is not None:
            # Remove the edge using the remove method of the edges DSALinkedList
            self.edges.remove(edgeToDelete)

            # Update adjacency information of the origin and destination vertices
            originVertex = self.getVertex(origin)
            destinationVertex = self.getVertex(destination)

            originVertex.getAdjacentVertex().remove(destinationVertex)
            destinationVertex.getAdjacentVertex().remove(originVertex)
            originVertex.getAdjacentEdge().remove(edgeToDelete)
            destinationVertex.getAdjacentEdge().remove(edgeToDelete)
    
    def displayGraphList(self, graphTitle: str = None):
        if graphTitle:
            print(graphTitle)
        print("Vertices:")
        for vertex in self.vertices:
            print(vertex)

        print("\nEdges:")
        for edge in self.edges:
            print(edge)

    def displayGraphMatrix(self):
        # Create a dictionary to map vertex labels to indices
        labelToIndex = {vertex.getLabel(): i for i, vertex in enumerate(self.vertices)}
        numVertices = self.getVertexCount()

        # Initialize the adjacency matrix with all zeros
        adjacencyMatrix = [[0] * numVertices for _ in range(numVertices)]

        # Fill in the matrix based on edges
        for edge in self.edges:
            originLabel = edge.getOrigin()
            destinationLabel = edge.getDestination()
            originIndex = labelToIndex[originLabel]
            destinationIndex = labelToIndex[destinationLabel]
            adjacencyMatrix[originIndex][destinationIndex] = 1
            adjacencyMatrix[destinationIndex][originIndex] = 1  # Assuming an undirected graph

        # Display the adjacency matrix
        print("Adjacency Matrix:")
        for row in adjacencyMatrix:
            print(" ".join(map(str, row)))

    def depthFirstSearch(self, startLabel, sort=False):
        # Check if the start vertex exists in the graph
        if not self.hasVertex(startLabel):
            raise ValueError("Start vertex does not exist")

        # Clear the 'visited' attribute for all vertices
        for vertex in self.vertices:
            vertex.clearVisited()

        # Get the start vertex
        startVertex = self.getVertex(startLabel)

        # Create a set to keep track of visited vertices within the same traversal
        visitedSet = set()

        # Create DSAStack (S)
        S = DSALinkedListStack()

        # Push the start vertex onto the stack
        S.push(startVertex)

        while not S.isEmpty():
            # Get the current vertex (top of the stack)
            v = S.peek()

            # If v has not been visited in this traversal, mark it as visited and print
            if v.getLabel() not in visitedSet:
                visitedSet.add(v.getLabel())
                print("Visited:", v.getLabel())
            
            # Find the next unvisited neighbor in v's adjacency list
            unvisitedNeighbors = [neighbor for neighbor in v.getAdjacentVertex() if neighbor.getLabel() not in visitedSet]

            if sort:
                # Sort the neighbors alphabetically if the 'sort' flag is True
                unvisitedNeighbors = sorted(unvisitedNeighbors, key=lambda x: x.getLabel())

            if unvisitedNeighbors:
                # Push the first unvisited neighbor onto the stack
                S.push(unvisitedNeighbors[0])
            else:
                # If there are no unvisited neighbors, pop the current vertex
                S.pop()


    def breadthFirstSearch(self, startLabel, sort=False):
        # Check if the start vertex exists in the graph
        if not self.hasVertex(startLabel):
            raise ValueError("Start vertex does not exist")

        # Clear the 'visited' attribute for all vertices
        for vertex in self.vertices:
            vertex.clearVisited()

        # Get the start vertex
        startVertex = self.getVertex(startLabel)

        # Set the start vertex as visited
        startVertex.setVisited()

        # Create two queues: T for traversal and Q for BFS
        T = DSALinkedListQueue()
        Q = DSALinkedListQueue()

        # Enqueue the start vertex into Q
        Q.enqueue(startVertex)

        while not Q.isEmpty():
            # Dequeue a vertex from the front of Q
            v = Q.dequeue()

            # Print the visited vertex's label
            print("Visited:", v.getLabel())

            unvisitedNeighbors = [neighbor for neighbor in v.getAdjacentVertex() if not neighbor.getVisited()]

            if sort:
                # Sort the neighbors alphabetically if the 'sort' flag is True
                unvisitedNeighbors = sorted(unvisitedNeighbors, key=lambda x: x.getLabel())


            # Iterate through adjacent vertices of v
            for w in v.getAdjacentVertex():
                if not w.getVisited():
                    # Enqueue v and w into T
                    T.enqueue(v)
                    T.enqueue(w)

                    # Set w as visited
                    w.setVisited()

                    # Enqueue w into Q for further exploration
                    Q.enqueue(w)


if __name__ == "__main__":
    print("Testing DSAGraphs.py")

    # Create a graph
    myGraph = DSAGraph()

    # Add vertices
    myGraph.addVertex("A", 10)
    myGraph.addVertex("B", 20)
    myGraph.addVertex("C", 30)
    myGraph.addVertex("D", 40)

    # Add edges
    myGraph.addEdge("A", "B", "Edge1", 100)
    myGraph.addEdge("A", "C", "Edge2", 200)
    myGraph.addEdge("B", "D", "Edge3", 300)

    # Check if vertices exist
    print("Vertex 'A' exists:", myGraph.hasVertex("A"))  # True
    print("Vertex 'E' exists:", myGraph.hasVertex("E"))  # False

    # Get vertex and edge counts
    print("Vertex count:", myGraph.getVertexCount())  # 4
    print("Edge count:", myGraph.getEdgeCount())      # 3

    # Get a specific vertex
    vertex_A = myGraph.getVertex("A")
    print("Vertex A:", vertex_A)  # Vertex - Label: A    Value: 10

    # Get a specific edge
    edge_AB = myGraph.getEdge("A", "B")
    print("Edge A-B:", edge_AB)  # Edge - Label: Edge1  Value: 100   Origin: A   Destination: B

    # Get adjacent vertices and edges
    adjacentVertices_A = myGraph.getAdjacentVertices("A")
    adjacentVertices_A.display("Adjacent vertices of A: ", ", ")  # ['B', 'C']

    adjacentEdges_A = myGraph.getAdjacentEdges("A")
    adjacentEdges_A.display("Adjacent edges of A:\n", "\n")
    # [Edge - Label: Edge1  Value: 100   Origin: A   Destination: B,
    #  Edge - Label: Edge2  Value: 200   Origin: A   Destination: C]

    # Print the graph's vertices and edges
    myGraph.displayGraphList("Test Graph as a List")
    myGraph.displayGraphMatrix()
    print("Depth-First Search:")
    myGraph.depthFirstSearch("A")
    print("Breadth-First Search:")
    myGraph.breadthFirstSearch("A")


# ShopGraph.py - part of the shop navigator project

from GraphDependencies.DSALinkedLists import DSALinkedList
from GraphDependencies.DSAqueues import DSALinkedListQueue
from GraphDependencies.DSAstack import DSALinkedListStack

class ShopGraph:
    def __init__(self):
        self.shopNodes = DSALinkedList()  # Create an instance of DSALinkedList for shop nodes
        self.paths = DSALinkedList()     # Create an instance of DSALinkedList for shop paths

    class ShopNode():
        def __init__(self, label, value):
            self.label = label
            self.value = value
            self.visited = False
            self.visitedInCurrentTraversal = False
            self.adjacentNodes = DSALinkedList()  # Create an instance of DSALinkedList for adjacent nodes
            self.adjacentPaths = DSALinkedList() # Create an instance of DSALinkedList for adjacent paths

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

        def addAdjacentNode(self, node):
            self.adjacentNodes.insertLast(node)

        def getAdjacentNode(self):
            return self.adjacentNodes
        
        def addAdjacentPath(self, path):
            self.adjacentPaths.insertLast(path)

        def getAdjacentPath(self):
            return self.adjacentPaths

        def __str__(self):
            return f"Unique ID: {self.label}\tShop Information --> {self.value}"

    class ShopPath():
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
            return f"Unique ID: {self.label}\tDistance: {self.value}\tOrigin: {self.origin}\tDestination: {self.destination}"

    def addShop(self, label, value) -> None:
        node = self.ShopNode(label, value)
        self.shopNodes.insertLast(node)

    def addPath(self, origin, destination, label, value) -> None:
        # Check if the origin and destination nodes exist
        if not self.hasShop(origin):
            raise ValueError("Origin " + origin + " does not exist")
        if not self.hasShop(destination):
            raise ValueError("Destination " + destination + " does not exist")


        # Create the path
        path = self.ShopPath(origin, destination, label, value)
        self.paths.insertLast(path)

        # Update the adjacency information for the nodes
        originNode = self.getShop(origin)
        destinationNode = self.getShop(destination)

        originNode.addAdjacentNode(destinationNode)
        destinationNode.addAdjacentNode(originNode)
        originNode.addAdjacentPath(path)
        destinationNode.addAdjacentPath(path)


    def hasShop(self, label):
        # Check if a node with the given label exists in the graph
        currentNode = self.shopNodes.head
        while currentNode is not None:
            if currentNode.getValue().getLabel() == label:
                return True
            currentNode = currentNode.getNext()
        return False

    def getShopCount(self) -> int:
        # Return the number of nodes in the graph
        return self.shopNodes.size()

    def getPathCount(self) -> int:
        # Return the number of paths in the graph
        return self.paths.size()

    def getShop(self, label) -> DSALinkedList.DSAListNode:
        # Return the node with the given label
        currentNode = self.shopNodes.head
        while currentNode is not None:
            if currentNode.getValue().getLabel() == label:
                return currentNode.getValue()
            currentNode = currentNode.getNext()
        raise ValueError("Shop does not exist")

    def getPath(self, origin, destination):
        # Return the path with the given labels
        currentPath = self.paths.head
        while currentPath is not None:
            path = currentPath.getValue()
            if (path.getOrigin() == origin and path.getDestination() == destination) or \
            (path.getOrigin() == destination and path.getDestination() == origin):
                return path
            currentPath = currentPath.getNext()
        raise ValueError("No direct path does not exist")

    def getAdjacentShops(self, label):
        # Return a list of adjacent nodes for the node with the given label
        node = self.getShop(label)
        nodes = DSALinkedList()
        if node:
            for v in node.getAdjacentNode():
                nodes.insertLast(v.getLabel())
        return nodes

    def getAdjacentPaths(self, label):
        # Return a list of adjacent paths for the node with the given label
        adjacentPaths = DSALinkedList()
        currentPath = self.paths.head
        while currentPath is not None:
            path = currentPath.getValue()
            if path.getOrigin() == label or path.getDestination() == label:
                adjacentPaths.insertLast(path)
            currentPath = currentPath.getNext()
        return adjacentPaths
    
    def editShopValue(self, label, newValue):
        # Check if the node exists
        if not self.hasShop(label):
            raise ValueError("Shop does not exist")

        # Get the node to be edited
        nodeToEdit = self.getShop(label)

        # Update the node's value
        nodeToEdit.value = newValue
    
    def deleteShop(self, label):
        # Check if the node exists
        if not self.hasShop(label):
            raise ValueError("Shop does not exist")

        # Get the node to be deleted
        nodeToDelete = self.getShop(label)

        # Remove all paths connected to the node
        for path in list(nodeToDelete.getAdjacentPath()):
            self.deletePath(path.getOrigin(), path.getDestination())

        # Remove the node from the list of nodes
        self.shopNodes.remove(nodeToDelete)

    def deletePath(self, origin, destination):
        # Check if both origin and destination nodes exist
        if not self.hasShop(origin):
            raise ValueError("Origin " + origin + " does not exist")
        if not self.hasShop(destination):
            raise ValueError("Destination " + destination + " does not exist")

        # Find the path to be deleted
        pathToDelete = None
        for path in self.paths:
            if (path.getOrigin() == origin and path.getDestination() == destination) or \
            (path.getOrigin() == destination and path.getDestination() == origin):
                pathToDelete = path
                break

        if pathToDelete is not None:
            # Remove the path using the remove method of the paths DSALinkedList
            self.paths.remove(pathToDelete)

            # Update adjacency information of the origin and destination nodes
            originNode = self.getShop(origin)
            destinationNode = self.getShop(destination)

            originNode.getAdjacentNode().remove(destinationNode)
            destinationNode.getAdjacentNode().remove(originNode)
            originNode.getAdjacentPath().remove(pathToDelete)
            destinationNode.getAdjacentPath().remove(pathToDelete)
    
    def displayGraphList(self, graphTitle: str = None):
        if self.shopNodes.size() == 0:
            raise RuntimeError("No Shops Created Yet")
        
        if graphTitle:
            print(graphTitle)
        print("Shops:")
        for node in self.shopNodes:
            print(node)

        print("\nPaths:")
        if self.paths.size() == 0:
            print("No Paths Exist")
        else:
            for path in self.paths:
                print(path)

    def displayGraphMatrix(self):
        if self.shopNodes.size() == 0:
            raise RuntimeError("No Shops Created Yet")
        
        # Create a dictionary to map node labels to indices
        labelToIndex = {node.getLabel(): i for i, node in enumerate(self.shopNodes)}
        numNodes = self.getShopCount()

        # Initialize the adjacency matrix with all zeros
        adjacencyMatrix = [[0] * numNodes for _ in range(numNodes)]

        # Fill in the matrix based on paths
        for path in self.paths:
            originLabel = path.getOrigin()
            destinationLabel = path.getDestination()
            originIndex = labelToIndex[originLabel]
            destinationIndex = labelToIndex[destinationLabel]
            adjacencyMatrix[originIndex][destinationIndex] = 1
            adjacencyMatrix[destinationIndex][originIndex] = 1  # Assuming an undirected graph

        # Display the adjacency matrix
        for row in adjacencyMatrix:
                print(" ".join(map(str, row)))

    def depthFirstSearch(self, startLabel, labelToFind=None, pathExistsCheck: bool = False, sortAlphabetically: bool = False):
        # Check if the start node exists in the graph
        if not self.hasShop(startLabel):
            raise ValueError("Start Shop does not exist")
        
        if labelToFind != None:
            if not self.hasShop(labelToFind):
                raise ValueError("End Shop does not exist")

        # Clear the 'visited' attribute for all nodes
        for node in self.shopNodes:
            node.clearVisited()

        # Get the start node
        startNode = self.getShop(startLabel)

        # Create a set to keep track of visited nodes within the same traversal
        visitedSet = set()

        # Create DSAStack (S)
        DFSStack = DSALinkedListStack()

        # Create Path List to store the path from one label to another
        path = DSALinkedList()

        # Push the start node onto the stack
        DFSStack.push(startNode)

        while not DFSStack.isEmpty():
            # Get the current node (top of the stack)
            v = DFSStack.peek()

            # If v has not been visited in this traversal, mark it as visited and add to path
            if v.getLabel() not in visitedSet:
                visitedSet.add(v.getLabel())
                path.insertLast(v.getLabel())

            # Check if the current node's label matches the labelToFind
            if labelToFind is not None and v.getLabel() == labelToFind:
                return path

            # Find the next unvisited neighbor in v's adjacency list
            unvisitedNeighbors = [neighbor for neighbor in v.getAdjacentNode() if neighbor.getLabel() not in visitedSet]

            if sortAlphabetically:
                # Sort the neighbors alphabetically if the 'sort' flag is True
                unvisitedNeighbors = sorted(unvisitedNeighbors, key=lambda x: x.getLabel())

            if unvisitedNeighbors:
                # Push the first unvisited neighbor onto the stack
                DFSStack.push(unvisitedNeighbors[0])
            else:
                # If there are no unvisited neighbors, pop the current node
                DFSStack.pop()

        #If pathExistsCheckl is True check that the path list contains the label to find then return path:
        if pathExistsCheck == True:
            if path.contains(labelToFind):
                return path
            else:
                raise RuntimeError("No Path Exists Between Shops")
        else:
            return path
            


    def breadthFirstSearch(self, startLabel, labelToFind=None, pathExistsCheck: bool = False, sortAlphabetically=False):
        # Check if the start node exists in the graph
        if not self.hasShop(startLabel):
            raise ValueError("Start Shop does not exist")
        
        if labelToFind != None:
            if not self.hasShop(labelToFind):
                raise ValueError("End Shop does not exist")


        # Clear the 'visited' attribute for all nodes
        for node in self.shopNodes:
            node.clearVisited()

        # Get the start node
        startNode = self.getShop(startLabel)

        # Set the start node as visited
        startNode.setVisited()

        # Create two queues: traversalQueue for traversal and BFSQueue for BFS
        traversalQueue = DSALinkedListQueue()
        BFSQueue = DSALinkedListQueue()

        # Create Path List to store the path from one label to another
        path = DSALinkedList()

        # Enqueue the start node into Q
        BFSQueue.enqueue(startNode)

        while not BFSQueue.isEmpty():
            # Dequeue a node from the front of BFSQueue
            v = BFSQueue.dequeue()

            # Add the visited node's label to path list
            path.insertLast(v.getLabel())

            # Check if the current node's label matches the labelToFind
            if labelToFind is not None and v.getLabel() == labelToFind:
                return path

            unvisitedNeighbors = [neighbor for neighbor in v.getAdjacentNode() if not neighbor.getVisited()]

            if sortAlphabetically:
                # Sort the neighbors alphabetically if the 'sort' flag is True
                unvisitedNeighbors = sorted(unvisitedNeighbors, key=lambda x: x.getLabel())

            # Iterate through adjacent nodes of v
            for adjacentV in unvisitedNeighbors:
                if not adjacentV.getVisited():
                    # Enqueue v and adjacentV into traversalQueue
                    traversalQueue.enqueue(v)
                    traversalQueue.enqueue(adjacentV)

                    # Set adjacentV as visited
                    adjacentV.setVisited()

                    # Enqueue adjacentV into Q for further exploration
                    BFSQueue.enqueue(adjacentV)

        #If pathExistsCheckl is True check that the path list contains the label to find then return path:
        if pathExistsCheck == True:
            if path.contains(labelToFind):
                return path
            else:
                raise RuntimeError("No Path Exists Between Shops")
        else:
            return path
        

    #Based on https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/?ref=gcse and modified for shopgraph
    def dijkstrasAlgorithm(self, startLabel, endLabel):
        # Check if the start and end nodes exist in the graph
        if not self.hasShop(startLabel) or not self.hasShop(endLabel):
            raise ValueError("Start or end shop does not exist")

        # Create dictionaries to store the minimum distance and the previous node in the path
        distance = {shop.getLabel(): float('inf') for shop in self.shopNodes}
        previous = {shop.getLabel(): None for shop in self.shopNodes}

        # Initialize the distance for the start node to 0
        distance[startLabel] = 0

        # Create a set to keep track of unvisited shops
        unvisited_shops = set(shop.getLabel() for shop in self.shopNodes)

        while unvisited_shops:
            # Find the shop with the smallest distance
            current_shop = min(unvisited_shops, key=lambda shop_label: distance[shop_label])

            # Remove the current shop from the set of unvisited shops
            unvisited_shops.remove(current_shop)

            # Exit the loop if the current shop is the end shop
            if current_shop == endLabel:
                break

            # Update the distance to the neighboring shops
            current_node = self.getShop(current_shop)
            for neighbor in current_node.getAdjacentNode():
                neighbor_label = neighbor.getLabel()
                path = self.getPath(current_shop, neighbor_label)
                if distance[current_shop] + path.getValue() < distance[neighbor_label]:
                    distance[neighbor_label] = distance[current_shop] + path.getValue()
                    previous[neighbor_label] = current_shop

        # Reconstruct the shortest path
        path = DSALinkedList()
        current_label = endLabel
        while current_label is not None:
            path.insertFirst(current_label)
            current_label = previous[current_label]

        if path.size() == 1:
            raise RuntimeError("No path exists between the shops")

        return path


if __name__ == '__main__':
    # Create a sample ShopGraph
    shop_graph = ShopGraph()

    # Add nodes and paths
    shop_graph.addShop("A", "Shop A")
    shop_graph.addShop("B", "Shop B")
    shop_graph.addShop("C", "Shop C")
    shop_graph.addShop("D", "Shop D")
    shop_graph.addShop("E", "Shop E")
    shop_graph.addShop("F", "Shop F")
    shop_graph.addShop("G", "Shop G")
    shop_graph.addPath("A", "B", "Path AB", 6)
    shop_graph.addPath("B", "C", "Path BC", 5)
    shop_graph.addPath("A", "C", "Path AC", 15)
    shop_graph.addPath("B", "D", "Path BD", 17)
    shop_graph.addPath("C", "E", "Path CE", 7)
    shop_graph.addPath("E", "F", "Path EF", 8)
    

    # Display the graph
    print("Initial ShopGraph:")
    shop_graph.displayGraphList()

    # Display the adjacency matrix
    print("Initial ShopGraph Matrix:")
    shop_graph.displayGraphMatrix()

    # Edit the value of node 'B'
    shop_graph.editShopValue("B", "New Shop B Value")

    # Display the graph to verify the edit
    print("ShopGraph after editing node 'B':")
    shop_graph.displayGraphList()

    # Test depth-first search
    print("\nDepth-First Search:")
    try:
        DFSResult = shop_graph.depthFirstSearch("C", "G", True)
        DFSResult.display("Path: ")
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)

    # Test breadth-first search
    print("\nBreadth-First Search:")
    try:
        BFSResult = shop_graph.breadthFirstSearch("C", "E", True)
        BFSResult.display("Path: ")
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)


    print("\nSearch using Dijkstra's Algorithm:")
    try:
        shortest_path = shop_graph.dijkstrasAlgorithm("A", "E")
        shortest_path.display(f"Shortest path :")
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)

    adjacentNodes_A = shop_graph.getAdjacentShops("A")
    adjacentNodes_A.display("\nAdjacent nodes of A: ", ", ")  # ['B', 'C']

    adjacentPaths_A =  shop_graph.getAdjacentPaths("A")
    adjacentPaths_A.display("\nAdjacent paths of A:\n", "\n")

    # Test node and path deletion
    shop_graph.deletePath("A", "C")
    shop_graph.deleteShop("B")
    print("\nShopGraph after deletion:")
    shop_graph.displayGraphList()

    # Display the adjacency matrix
    print("ShopGraph Matrix:")
    shop_graph.displayGraphMatrix()

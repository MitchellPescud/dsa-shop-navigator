# DSALinkedLists.py - part of the shop navigator project
import numpy as np

class DSALinkedList:
    """
    A doubly linked list data structure implementation.

    This class provides methods to manage and manipulate a doubly linked list.
    Each element in the list is encapsulated within a DSAListNode object.
    """
    class DSAListNode:
        """
        Node class for a doubly linked list.

        Attributes:
            value: The value stored in the node.
            next: Reference to the next node in the linked list.
            prev: Reference to the previous node in the linked list.
        """
        def __init__(self, inValue):
            """
            Initialize a new node.

            Args:
                inValue (Any): The value to store in the node.
            """
            self.value = inValue
            self.next = None
            self.prev = None

        def getValue(self):
            """
            Get the value stored in the node.

            Returns:
                Any: The value stored in the node.
            """
            return self.value

        def setValue(self, inValue):
            """
            Set the value of the node.

            Args:
                inValue (Any): The new value to set.
            """
            self.value = inValue

        def getNext(self):
            """
            Get the reference to the next node.

            Returns:
                DSAListNode: Reference to the next node.
            """
            return self.next

        def setNext(self, newNext):
            """
            Set the reference to the next node.

            Args:
                newNext (DSAListNode): The new next node to set.
            """
            self.next = newNext

        def getPrev(self):
            """
            Get the reference to the previous node.

            Returns:
                DSAListNode: Reference to the previous node.
            """
            return self.prev

        def setPrev(self, newPrev):
            """
            Set the reference to the previous node.

            Args:
                newPrev (DSAListNode): The new previous node to set.
            """
            self.prev = newPrev

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insertFirst(self, newValue):
        """
        Insert a new value at the beginning of the linked list.

        Args:
            newValue (Any): The value to insert.
        """
        newNode = self.DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
            
    def insertLast(self, newValue):
        """
        Insert a new value at the end of the linked list.

        Args:
            newValue (Any): The value to insert.
        """
        newNode = self.DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setPrev(self.tail)
            self.tail.setNext(newNode)
            self.tail = newNode

    def isEmpty(self) -> bool:
        """
        Check if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

    def peekFirst(self):
        """
        Get the value of the first node without removing it.

        Returns:
            Any: The value of the first node.
        """
        if self.isEmpty():
            raise IndexError("peekFirst failed! List is empty")
        return self.head.getValue()

    def peekLast(self):
        """
        Get the value of the last node without removing it.

        Returns:
            Any: The value of the last node.
        """
        if self.isEmpty():
            raise IndexError("peekLast failed! List is empty")
        return self.tail.getValue()

    def removeFirst(self):
        """
        Remove and return the value of the first node.

        Returns:
            Any: The value of the removed first node.
        """
        if self.isEmpty():
            raise IndexError("removeFirst failed! List is empty")
        nodeValue = self.head.getValue()
        self.head = self.head.getNext()
        if self.head is not None:
            self.head.setPrev(None)  # Update previous reference of the new head
        return nodeValue

    def removeLast(self):
        """
        Remove and return the value of the last node.

        Returns:
            Any: The value of the removed last node.
        """
        if self.isEmpty():
            raise IndexError("removeLast failed! List is empty")
        elif self.head.getNext() is None:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
            return nodeValue
        else:
            currentNode = self.tail
            previousNode = currentNode.getPrev()
            nodeValue = currentNode.getValue()
            previousNode.setNext(None)
            self.tail = previousNode
            return nodeValue
        
    def remove(self, targetValue):
        """
        Remove the first occurrence of the specified value from the linked list.

        Args:
            targetValue (Any): The value to remove.

        Returns:
            bool: True if the value was found and removed, False otherwise.
        """
        currentNode = self.head

        while currentNode is not None:
            if currentNode.getValue() == targetValue:
                if currentNode is self.head:
                    # If the target value is in the first node
                    self.removeFirst()
                elif currentNode is self.tail:
                    # If the target value is in the last node
                    self.removeLast()
                else:
                    # If the target value is in an intermediate node
                    prevNode = currentNode.getPrev()
                    nextNode = currentNode.getNext()
                    prevNode.setNext(nextNode)
                    nextNode.setPrev(prevNode)
                return True

            currentNode = currentNode.getNext()

        return False
        
    def size(self) -> int:
        """
        Calculate and return the size of the linked list.

        Returns:
            int: The number of elements in the linked list.
        """
        count = 0
        currentNode = self.head
        while currentNode is not None:
            count += 1
            currentNode = currentNode.getNext()
        return count

    def display(self, message: str = "List contents: ", separator: str =" -> ") -> None:
        """
        Display a custom message inline with the items in the linked list, with handling for an empty list.

        Args:
            message (str, optional): The custom message to display. Default is "List contents:".
            separator (str, optional): The separator between the message and the list elements. Default is " -> ".
        """
        if self.isEmpty():
            print("List is empty")
        else:
            elements = []
            currentNode = self.head
            while currentNode is not None:
                elements.append(str(currentNode.getValue()))
                currentNode = currentNode.getNext()
            print("{}{}".format(message, separator.join(elements)))

    def __iter__(self):
        currentNode = self.head
        while currentNode is not None:
            yield currentNode.getValue()
            currentNode = currentNode.getNext()

    def contains(self, targetValue):
        """
        Check if the list contains a specific value.

        Args:
            targetValue (Any): The value to check for.

        Returns:
            bool: True if the value is found in the list, False otherwise.
        """
        for value in self:
            if value == targetValue:
                return True
        return False
    
    def toNumpyArray(self):
        """
        Convert the linked list data to a NumPy array.

        Returns:
            numpy.ndarray: A NumPy array containing the data from the linked list.
        """
        data_list = list(self)  # Use the __iter__ method to collect data into a list
        return np.array(data_list)

            
# Example usage
if __name__ == "__main__":
    myList = DSALinkedList()

    # Insert values
    myList.insertFirst(10)
    myList.insertLast(20)
    myList.insertLast(30)
    myList.insertFirst(0)

    # Print the list
    print("List after insertion:")
    myList.display()

    # Calculate and print the size
    print("\nSize of the list:", myList.size())

    # Test peek methods
    print("\nFirst value:", myList.peekFirst())  # Output: First value: 10
    print("Last value:", myList.peekLast())    # Output: Last value: 30

    # Test removal methods
    print("Removed first:", myList.removeFirst())  # Output: Removed first: 10
    print("Removed last:", myList.removeLast())    # Output: Removed last: 30

    # Print the list after removal
    print("\nList after removal:")
    myList.display()

    # Check if the list is empty
    print("\nIs empty?", myList.isEmpty())  # Output: Is empty? False

    print("Removed first:", myList.removeFirst())
    print("Removed last:", myList.removeLast())

    print("\nIs empty?", myList.isEmpty()) 
    myList.display()
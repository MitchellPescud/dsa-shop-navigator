from HeapDependencies.DSAHeapEntry import DSAHeapEntry
import numpy as np

class DSAHeap:
    def __init__(self, defaultCapacity: int = 10) -> None:
        """
        Initialize a DSAHeap instance with an optional default capacity.

        Args:
            defaultCapacity (int, optional): The default capacity of the heap. Defaults to 10.
        """
        self.capacity = defaultCapacity
        self.heapArray = np.empty(self.capacity, dtype=object)
        self.count = 0
        
    def add(self, priority: int, value: object) -> None:
        """
        Add a new entry with a specified priority and value to the heap.

        Args:
            priority (int): The priority of the entry.
            value (object): The value associated with the entry.
        """
        if self.count == self.capacity:
            # Double the capacity if the heap is full
            self.capacity *= 2
            newHeapArray = np.empty(self.capacity, dtype=object)
            newHeapArray[:self.count] = self.heapArray
            self.heapArray = newHeapArray
        
        # Create a new DSAHeapEntry with the given priority and value
        newEntry = DSAHeapEntry(priority, value)

        # Add the new entry to the end of the heap
        self.heapArray[self.count] = newEntry
        self.count += 1

        # Maintain the heap property by trickling up the newly added entry
        self.trickleUp(self.count-1)

    def remove(self) -> DSAHeapEntry:
        """
        Remove and return the entry with the highest priority from the heap.

        Returns:
            DSAHeapEntry: The entry with the highest priority.
        """
        if self.count == 0:
            raise IndexError("Heap is empty, cannot remove.")

        # Remove the root element (highest priority) from the heap
        root = self.heapArray[0]

        # Replace the root with the last element in the heap
        self.count -= 1
        self.heapArray[0] = self.heapArray[self.count]

        # Maintain the heap property by trickling down the new root
        self.trickleDown(0)

        return root

    def trickleUp(self, index: int) -> None:
        """
        Perform the trickle-up operation to maintain the heap property.

        Args:
            index (int): The index of the element to start the trickle-up operation from.
        """
        while index > 0 and self.heapArray[index].getPriority() > self.heapArray[(index - 1) // 2].getPriority():
            # Swap the elements at index and parentIndex
            self.heapArray[index], self.heapArray[(index - 1) // 2] = self.heapArray[(index - 1) // 2], self.heapArray[index]
            index = (index - 1) // 2

    def trickleDown(self, index: int) -> None:
        """
        Perform the trickle-down operation to maintain the heap property.

        Args:
            index (int): The index of the element to start the trickle-down operation from.
        """
        lChildIndex = index * 2 + 1
        rChildIndex = lChildIndex + 1
        keepTrickling = True
        while keepTrickling == True and lChildIndex < self.count:
            keepTrickling = False
            largeIndex = lChildIndex
            if rChildIndex < self.count and self.heapArray[lChildIndex].getPriority() < self.heapArray[rChildIndex].getPriority():
                largeIndex = rChildIndex
            if self.heapArray[largeIndex].getPriority() > self.heapArray[index].getPriority():
                # Swap the elements at largeIndex and index
                self.heapArray[largeIndex], self.heapArray[index] = self.heapArray[index], self.heapArray[largeIndex]
                # Continue trickling down the swapped element
                index = largeIndex
                lChildIndex = index * 2 + 1
                rChildIndex = lChildIndex + 1
                keepTrickling = True

    def displayArray(self) -> None:
        """
        Display the elements in the heap in array format.
        """
        if self.count == 0:
            print("Heap is empty.")
            return

        for i in range(self.count):
            entry: DSAHeapEntry = self.heapArray[i]
            print(f"Priority: {entry.getPriority()}, Value: {entry.getValue()}")

    def displayTree(self):
        """
        Display the elements in the heap in tree format.
        """
        if self.count == 0:
            print("Heap is empty.")
            return

        self.displayTreeRecursive(0, 0)

    def displayTreeRecursive(self, index, depth):
        """
        Recursively display the elements in the heap in tree format.

        Args:
            index (int): The index of the current element.
            depth (int): The depth of the current element in the heap.
        """
        if index >= self.count:
            return

        # Print the current node's priority and value
        entry: DSAHeapEntry = self.heapArray[index]
        print(f"{'  ' * depth}Priority: {entry.getPriority()}, Value: {entry.getValue()}")

        # Recursively print the left and right children
        lChildIndex = index * 2 + 1
        rChildIndex = lChildIndex + 1
        self.displayTreeRecursive(lChildIndex, depth + 1)
        self.displayTreeRecursive(rChildIndex, depth + 1)

if __name__ == "__main__":
    # Create a DSAHeap instance
    heap = DSAHeap()

    # Add some elements to the heap
    heap.add(5, "Apple")
    heap.add(3, "Banana")
    heap.add(8, "Cherry")
    heap.add(1, "Date")
    heap.add(9, "Passionfruit")
    heap.add(7, "Fig")
    heap.add(100, "Blackcurrant")
    heap.add(921, "Grape")

    # Display the heap
    print("\nHeap after adding elements (Array Format):")
    heap.displayArray()
    print("\nHeap after adding elements (Tree Format):")
    heap.displayTree()

    # Remove elements from the heap
    print("\nRemoving elements from the heap:")
    entry = heap.remove()
    print(f"Removed: Priority {entry.getPriority()}, Value: {entry.getValue()}")
    entry = heap.remove()
    print(f"Removed: Priority {entry.getPriority()}, Value: {entry.getValue()}")

    # Display the heap after removal
    print("\nHeap after removing elements (Array Format):")
    heap.displayArray()
    print("\nHeap after removing elements (Tree Format):")
    heap.displayTree()

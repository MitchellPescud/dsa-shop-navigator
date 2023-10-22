# DSAqueues.py - part of the shop navigator project
import numpy as np
from GraphDependencies.DSALinkedLists import DSALinkedList

class DSAQueue:
    """
    A class representing a queue data structure that can use either shuffling or circular implementation.

    Methods:
        __init__(self, queueType: str, maxCapacity: int = None):
            Initializes a new DSAQueue instance with a specified queue type and maximum capacity.
        
        enqueue(self, item):
            Enqueues an item into the queue.
            
        dequeue(self):
            Dequeues an item from the queue and returns it.
            
        peek(self):
            Returns the item at the front of the queue without removing it.
            
        isEmpty(self) -> bool:
            Checks if the queue is empty.
            
        isFull(self) -> bool:
            Checks if the queue is full.
            
        size(self) -> int:
            Returns the current size of the queue.
            
        display(self, CustomText: str = "Queue:"):
            Displays the contents of the queue, with an optional custom text prefix.
    """
    class ShufflingQueue:
        """
        A class representing a shuffling queue data structure.

        This queue uses a shuffling method for enqueue and dequeue operations, ensuring fairness
        in accessing elements even with frequent enqueues and dequeues.

        Methods:
            __init__(self, maxCapacity: int = None):
                Initializes a new ShufflingQueue instance.

            isEmpty(self) -> bool:
                Checks if the shuffling queue is empty.

            isFull(self) -> bool:
                Checks if the shuffling queue is full.

            enqueue(self, item):
                Enqueues an item into the shuffling queue.

            dequeue(self):
                Dequeues an item from the shuffling queue and returns it.

            peek(self):
                Gets the item at the front of the shuffling queue without removing it.

            size(self) -> int:
                Gets the current size of the shuffling queue.

            display(self, customText: str = "Queue:") -> None:
                Displays the contents of the shuffling queue, with an optional custom text prefix.
        """
        DEFAULT_CAPACITY = 100

        def __init__(self, maxCapacity=None):
            """
            Initializes a new ShufflingQueue instance.

            Args:
                maxCapacity (int, optional): The maximum capacity of the queue. Defaults to DEFAULT_CAPACITY (100).
            """
            if maxCapacity is None:
                maxCapacity = self.DEFAULT_CAPACITY
            self.queue = np.zeros(maxCapacity, dtype=object)
            self.count = 0

        def isEmpty(self) -> bool:
            """
            Checks if the shuffling queue is empty.

            Returns:
                bool: True if the queue is empty, False otherwise.
            """
            return self.count == 0

        def isFull(self) -> bool:
            """
            Checks if the shuffling queue is full.

            Returns:
                bool: True if the queue is full, False otherwise.
            """
            return self.count == len(self.queue)

        def enqueue(self, item):
            """
            Enqueues an item into the shuffling queue.

            Args:
                item (any): The item to be enqueued.
            """
            if self.count < len(self.queue):
                self.queue[self.count] = item
                self.count += 1
            else:
                raise IndexError("Queue is full")

        def dequeue(self):
            """
            Dequeues an item from the shuffling queue and returns it.

            Returns:
                The dequeued item.
            """
            if self.count > 0:
                item = self.queue[0]
                for i in range(self.count - 1):
                    self.queue[i] = self.queue[i + 1]
                self.count -= 1
                return item
            else:
                raise IndexError("Queue is empty")

        def peek(self):
            """
            Gets the item at the front of the shuffling queue without removing it.

            Returns:
                The item at the front of the queue.
            """
            if self.count > 0:
                return self.queue[0]
            else:
                raise IndexError("Queue is empty")

        def size(self) -> int:
            """
            Gets the current size of the shuffling queue.

            Returns:
                int: The current size of the queue.
            """
            return self.count

        def display(self, customText: str = "Queue:") -> None:
            """
            Displays the contents of the shuffling queue, with an optional custom text prefix.

            Args:
                customText (str): Custom text to be displayed before the queue contents.
            """
            if self.isEmpty():
                print("Queue is empty")
                return
            
            print(customText, end="")
            for i in range(self.count):
                print(self.queue[i], end=" ")
            print()

    class CircularQueue:
        """
        A class representing a circular queue data structure.

        This queue uses a circular method for enqueue and dequeue operations, allowing efficient
        space utilization and continuous operation without the need to shift elements.

        Methods:
            __init__(self, maxCapacity: int = None):
                Initializes a new CircularQueue instance.

            isEmpty(self) -> bool:
                Checks if the circular queue is empty.

            isFull(self) -> bool:
                Checks if the circular queue is full.

            enqueue(self, item):
                Enqueues an item into the circular queue.

            dequeue(self):
                Dequeues an item from the circular queue and returns it.

            peek(self):
                Gets the item at the front of the circular queue without removing it.

            size(self) -> int:
                Gets the current size of the circular queue.

            display(self, customText: str = "Queue: ") -> None:
                Displays the contents of the circular queue, with an optional custom text prefix.
        """
        DEFAULT_CAPACITY = 100
        
        def __init__(self, maxCapacity=None):
            """
            Initializes a new CircularQueue instance.

            Args:
                maxCapacity (int, optional): The maximum capacity of the queue. Defaults to DEFAULT_CAPACITY (100).
            """
            if maxCapacity is None:
                maxCapacity = self.DEFAULT_CAPACITY
            
            self.queue = np.zeros(maxCapacity, dtype=object)
            self.count = 0
            self.front = 0
            self.rear = -1
            self.maxCapacity = maxCapacity
        
        def isEmpty(self) -> bool:
            """
            Checks if the circular queue is empty.

            Returns:
                bool: True if the queue is empty, False otherwise.
            """
            return self.count == 0
        
        def isFull(self) -> bool:
            """
            Checks if the circular queue is full.

            Returns:
                bool: True if the queue is full, False otherwise.
            """
            return self.count == self.maxCapacity
        
        def enqueue(self, item):
            """
            Enqueues an item into the circular queue.

            Args:
                item (any): The item to be enqueued.
            """
            if self.isFull():
                raise ValueError("Queue is full")
            
            self.rear = (self.rear + 1) % self.maxCapacity
            self.queue[self.rear] = item
            self.count += 1
        
        def dequeue(self):
            """
            Dequeues an item from the circular queue and returns it.

            Returns:
                The dequeued item.
            """
            if self.isEmpty():
                raise ValueError("Queue is empty")
            
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxCapacity
            self.count -= 1
            return item
        
        def peek(self):
            """
            Gets the item at the front of the circular queue without removing it.

            Returns:
                The item at the front of the queue.
            """
            if self.isEmpty():
                raise ValueError("Queue is empty")
            
            return self.queue[self.front]
        
        def size(self) -> int:
            """
            Gets the current size of the circular queue.

            Returns:
                int: The current size of the queue.
            """
            return self.count
        
        def display(self, customText: str = "Queue: ") -> None:
            """
            Displays the contents of the circular queue, with an optional custom text prefix.

            Args:
                customText (str): Custom text to be displayed before the queue contents.
            """
            if self.isEmpty():
                print("Queue is empty")
                return
            
            print(customText, end="")
            current = self.front
            while True:
                print(self.queue[current], end=" ")
                if current == self.rear:
                    break
                current = (current + 1) % self.maxCapacity
            print()

    def __init__(self, queueType: str, maxCapacity: int = None):
        """
        Initializes a new DSAQueue instance with a specified queue type and maximum capacity.

        Args:
            queueType (str): A string indicating the type of queue to use ("shuffling" or "circular").
            maxCapacity (int) (optional): An integer representing the maximum capacity of the queue. Default capacity is 100.
        """
        if queueType == "shuffling":
            self.queue = self.ShufflingQueue(maxCapacity)
        elif queueType == "circular":
            self.queue = self.CircularQueue(maxCapacity)
        else:
            raise ValueError("Invalid queue type")

    def enqueue(self, item):
        """
        Enqueues an item into the queue.

        Args:
            item: The item to be enqueued.
        """
        self.queue.enqueue(item)

    def dequeue(self):
        """
        Dequeue an item from the queue and return it.

        Returns:
            The dequeued item.
        """
        return self.queue.dequeue()

    def peek(self):
        """
        Get the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.
        """
        return self.queue.peek()

    def isEmpty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.queue.isEmpty()

    def isFull(self) -> bool:
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.queue.isFull()

    def size(self) -> int:
        """
        Gets the current size of the queue.

        Returns:
            int: The current size of the queue.
        """
        return self.queue.size()

    def display(self, CustomText: str = "Queue:"):
        """
        Displays the contents of the queue, with an optional custom text prefix.

        Args:
            CustomText (str): Custom text to be displayed before the queue contents.
        """
        self.queue.display(CustomText)

class DSALinkedListQueue:
    """
    Represents a queue implemented using a doubly-ended, doubly-linked list.

    This class provides the following basic queue operations:
    - enqueue: Add an item to the back of the queue.
    - dequeue: Remove and retrieve the item from the front of the queue.
    - peek: Retrieve the item at the front of the queue without removal.
    - isEmpty: Check if the queue is empty.
    - size: Get the current size of the queue.

    Attributes:
        queue (DSALinkedList): A DSALinkedList instance serving as the underlying data structure for the queue.
    """
    def __init__(self):
        """
         Initializes a new queue based on DSALinkedLists double ended, doubly linked list.
        """
        self.queue = DSALinkedList()

    def isEmpty(self) -> bool:
        """
        Checks if the shuffling queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.queue.isEmpty()

    def enqueue(self, item):
        """
        Enqueues an item into the shuffling queue.

        Args:
            item (any): The item to be enqueued.
        """
        self.queue.insertLast(item)

    def dequeue(self):
        """
        Dequeues an item from the shuffling queue and returns it.

        Returns:
            The dequeued item.
        """
        return self.queue.removeFirst()

    def peek(self):
        """
        Gets the item at the front of the shuffling queue without removing it.

        Returns:
            The item at the front of the queue.
        """
        return self.queue.peekFirst()

    def size(self) -> int:
        """
        Gets the current size of the shuffling queue.

        Returns:
            int: The current size of the queue.
        """
        return self.queue.size()

    def display(self, customText: str = "Queue:") -> None:
        """
        Displays the contents of the shuffling queue, with an optional custom text prefix.

        Args:
            customText (str): Custom text to be displayed before the queue contents.
        """
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            self.queue.display(customText)

if __name__ == "__main__":
    # Test ShufflingQueue
    print("Testing ShufflingQueue:")
    shufflingQueue = DSAQueue("shuffling", maxCapacity=5)
    shufflingQueue.enqueue(1)
    shufflingQueue.enqueue(2)
    shufflingQueue.enqueue(3)
    shufflingQueue.enqueue(4)
    shufflingQueue.enqueue(5)

    print("Enqueued elements: 1, 2, 3, 4, 5")
    print("Is full?", shufflingQueue.isFull())
    shufflingQueue.display("Shuffling Queue: ")

    print("Dequeued element:", shufflingQueue.dequeue())
    print("Dequeued element:", shufflingQueue.dequeue())

    print("Peeked element:", shufflingQueue.peek())
    print("Is empty?", shufflingQueue.isEmpty())
    print("Is full?", shufflingQueue.isFull())
    print("Queue size:", shufflingQueue.size())

    shufflingQueue.display("Shuffling Queue: ")
    print("="*30)

    # Test CircularQueue
    print("Testing CircularQueue:")
    circularQueue = DSAQueue("circular", maxCapacity=5)
    circularQueue.enqueue(10)
    circularQueue.enqueue(20)
    circularQueue.enqueue(30)
    circularQueue.enqueue(40)

    print("Enqueued elements: 10, 20, 30, 40")
    circularQueue.display("Circular Queue: ")

    print("Dequeued element:", circularQueue.dequeue())
    print("Dequeued element:", circularQueue.dequeue())

    print("Peeked element:", circularQueue.peek())
    print("Is empty?", circularQueue.isEmpty())
    print("Is full?", circularQueue.isFull())
    print("Queue size:", circularQueue.size())

    circularQueue.display("Circular Queue: ")
    print("="*30)

    # Test DSALinkedListQueue
    print("Testing DSALinkedListQueue:")
    linkedListQueue = DSALinkedListQueue()
    linkedListQueue.enqueue("A")
    linkedListQueue.enqueue("B")
    linkedListQueue.enqueue("C")

    print("Enqueued elements: A, B, C")
    linkedListQueue.display("Linked List Queue:")

    print("Dequeued element:", linkedListQueue.dequeue())
    print("Dequeued element:", linkedListQueue.dequeue())

    print("Peeked element:", linkedListQueue.peek())
    print("Is empty?", linkedListQueue.isEmpty())
    print("Queue size:", linkedListQueue.size())

    linkedListQueue.display("Linked List Queue: ")

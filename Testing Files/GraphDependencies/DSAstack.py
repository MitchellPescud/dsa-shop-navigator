# DSAstack.py - part of the shop navigator project
import numpy as np
from GraphDependencies.DSALinkedLists import DSALinkedList

class DSAStack:
    """
    A class representing a stack data structure.
    
    Attributes:
        DEFAULT_CAPACITY (int): The default maximum capacity of the stack.
        
    Methods:
        __init__(self, maxCapacity: int = None):
            Initializes a new DSAStack instance.
        
        isEmpty(self) -> bool:
            Checks if the stack is empty.
            
        isFull(self) -> bool:
            Checks if the stack is full.
            
        push(self, item):
            Pushes an item onto the top of the stack.
            
        pop(self):
            Removes and returns the top item from the stack.
            
        peek(self):
            Returns the top item from the stack without removing it.
            
        size(self) -> int:
            Returns the current number of items in the stack.
            
        display(self, customText: str = None, outputTopToBottom: bool = True) -> None:
            Displays the contents of the stack, with options for customization.
    """
    DEFAULT_CAPACITY = 100
    
    def __init__(self, maxCapacity: int = None):
        """
        Initializes a new DSAStack instance.
        
        Args:
            maxCapacity (int, optional): The maximum capacity of the stack. Defaults to DEFAULT_CAPACITY (100).
        """
        if maxCapacity is None:
            maxCapacity = DSAStack.DEFAULT_CAPACITY
            
        self.stack = np.zeros(maxCapacity, dtype=object)
        self.count = 0

    def isEmpty(self) -> bool:
        """
        Checks if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.count == 0
    
    def isFull(self) -> bool:
        """
        Checks if the stack is full.
        
        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return self.count == len(self.stack)
    
    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        
        Args:
            item: The item to be pushed onto the stack.
        """
        if self.isFull():
            raise ValueError("Stack is full")
        self.stack[self.count] = item
        self.count += 1
        return self
    
    def pop(self):
        """
        Removes and returns the top item from the stack.
        
        Returns:
            The top item that was removed from the stack.
        
        Raises:
            ValueError: If the stack is empty.
        """
        if self.isEmpty():
            raise ValueError("Stack is empty")
        self.count -= 1
        return self.stack[self.count]
    
    def peek(self):
        """
        Returns the top item from the stack without removing it.
        
        Returns:
            The top item of the stack.
            
        Raises:
            ValueError: If the stack is empty.
        """
        if self.isEmpty():
            raise ValueError("Stack is empty")
        return self.stack[self.count - 1]
    
    def size(self) -> int:
        """
        Returns the current number of items in the stack.
        
        Returns:
            int: The number of items in the stack.
        """
        return self.count
    
    def display(self, customText: str = None, outputTopToBottom: bool = True) -> None:
        """
        Displays the contents of the stack, with options for customization.
        
        Args:
            customText (str, optional): Custom text to be displayed before the stack contents. Defaults to None.
            outputTopToBottom (bool, optional): Determines whether to display the stack from top to bottom. Defaults to True.
        """
        if self.isEmpty():
            print("Stack is empty")
            return
        
        if outputTopToBottom:
            if customText != None:
                print(customText + ": [", end="")
            else:
                print("Stack (Top to Bottom): [", end="")
            print(", ".join(repr(item) for item in self.stack[self.count - 1::-1]), end="]\n")
            return ""
        else:
            if customText != None:
                print(customText + ": [", end="")
            else:
                print("Stack (Bottom to Top): [", end="")
            print(", ".join(repr(item) for item in self.stack[:self.count]), end="]\n")
            return ""

class DSALinkedListStack:
    """
    A class representing a stack data structure using a double ended, doubly-linked list.
         
    Methods:
        __init__(self):
            Initializes a new DSALinkedListStack instance.
        
        isEmpty(self) -> bool:
            Checks if the stack is empty.
            
        push(self, item):
            Pushes an item onto the top of the stack.
            
        pop(self):
            Removes and returns the top item from the stack.
            
        peek(self):
            Returns the top item from the stack without removing it.
            
        size(self) -> int:
            Returns the current number of items in the stack.
            
        display(self, customText: str = None) -> None:
            Displays the contents of the stack, with options for customization.
    """
    
    def __init__(self):
        """
        Initializes a new DSAStack instance.
        """
        self.stack = DSALinkedList()

    def isEmpty(self) -> bool:
        """
        Checks if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.stack.isEmpty()
    
    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        
        Args:
            item: The item to be pushed onto the stack.
        """
        self.stack.insertFirst(item)
    
    def pop(self):
        """
        Removes and returns the top item from the stack.
        
        Returns:
            The top item that was removed from the stack.
        """
        return self.stack.removeFirst()
    
    def peek(self):
        """
        Returns the top item from the stack without removing it.
        
        Returns:
            The top item of the stack.
        """
        return self.stack.peekFirst()
    
    def size(self) -> int:
        """
        Returns the current number of items in the stack.
        
        Returns:
            int: The number of items in the stack.
        """
        return self.stack.size()
    
    def display(self, customText: str = None) -> None:
        """
        Displays the contents of the stack, with options for customization.
        
        Args:
            customText (str, optional): Custom text to be displayed before the stack contents. Defaults to None.
        """
        self.stack.display(customText)

if __name__ == "__main__":
    # Testing DSAStack
    print("Testing DSAStack:")
    stack = DSAStack(maxCapacity=3)

    print("Is Empty?", stack.isEmpty())  # Should print True

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.display("Stack Contents")  # Should print the stack contents

    print("Is Empty?", stack.isEmpty())  # Should print False
    print("Is Full?", stack.isFull())  # Should print True

    print("Peek:", stack.peek())  # Should print the top item (3)
    print("Pop:", stack.pop())  # Should print and remove the top item (3)

    stack.display("Updated Stack Contents")
    print("="*30)
    # Testing DSALinkedListStack
    print("Testing DSALinkedListStack:")
    llStack = DSALinkedListStack()

    print("Is Empty?", llStack.isEmpty())  # Should print True

    llStack.push("A")
    llStack.push("B")
    llStack.push("C")

    llStack.display("Stack Contents")  # Should print the stack contents

    print("Is Empty?", llStack.isEmpty())  # Should print False

    print("Peek:", llStack.peek())  # Should print the top item ("C")
    print("Pop:", llStack.pop())  # Should print and remove the top item ("C")

    llStack.display("Updated Stack Contents")

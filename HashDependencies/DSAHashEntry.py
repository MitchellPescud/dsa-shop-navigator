# DSAHashEntry.py - part of the shop navigator project

class DSAHashEntry:
    """
    A class representing an entry in a hash table.
    
    Attributes:
        key (str): The key associated with the entry.
        value (object): The value associated with the entry.
        state (int): The state of the entry (0 for empty, 1 for occupied, -1 for previously occupied).
    """

    def __init__(self, key: str = None, value: object = None) -> None:
        """
        Initialize a new DSAHashEntry.

        Args:
            key (str, optional): The key for the entry.
            value (object, optional): The value for the entry.
        """
        self.key: str = key if key is not None else ""
        self.value: object = value
        self.state: int = 1 if key is not None else 0

    def getKey(self) -> str:
        """
        Get the key of the entry.

        Returns:
            str: The key associated with the entry.
        """
        return self.key
    
    def getValue(self) -> object:
        """
        Get the value of the entry.

        Returns:
            object: The value associated with the entry.
        """
        return self.value
    
    def getState(self) -> int:
        """
        Get the state of the entry.

        Returns:
            int: The state of the entry (0 for empty, 1 for occupied, -1 for previously occupied).
        """
        return self.state
    
    def setKey(self, key: str) -> None:
        """
        Set the key of the entry.

        Args:
            key (str): The new key to set.
        """
        self.key = key
    
    def setValue(self, value: object) -> None:
        """
        Set the value of the entry.

        Args:
            value (object): The new value to set.
        """
        self.value = value
    
    def setState(self, state: int) -> None:
        """
        Set the state of the entry.

        Args:
            state (int): The new state to set (0 for empty, 1 for occupied, -1 for previously occupied).
        """
        self.state = state



if __name__ == "__main__":
    # Create some DSAHashEntry objects
    entry1 = DSAHashEntry("name", "Alice")
    entry2 = DSAHashEntry("age", 30)
    entry3 = DSAHashEntry()
    entry4 = DSAHashEntry("name", "John")

    # Test getKey, getValue, and getState methods
    print("Entry 1:")
    print("Key:", entry1.getKey())
    print("Value:", entry1.getValue())
    print("State:", entry1.getState())

    print("\nEntry 2:")
    print("Key:", entry2.getKey())
    print("Value:", entry2.getValue())
    print("State:", entry2.getState())

    print("\nEntry 3:")
    print("Key:", entry3.getKey())
    print("Value:", entry3.getValue())
    print("State:", entry3.getState())

    print("\nEntry 4:")
    print("Key:", entry4.getKey())
    print("Value:", entry4.getValue())
    print("State:", entry4.getState())

    # Update key and value
    entry4.setKey("age")
    entry4.setValue(40)

    # Test methods again
    print("Updated Key:", entry4.getKey())
    print("Updated Value:", entry4.getValue())

    # Set state to 0
    entry4.setState(0)
    print("Updated State:", entry4.getState())
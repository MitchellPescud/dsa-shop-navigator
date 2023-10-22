class DSAHeapEntry:
    """
    Represents an entry in a Priority Queue (Heap) data structure with a priority and a value.

    Attributes:
        priority (int): The priority of the entry.
        value (object): The value associated with the entry.
    """

    def __init__(self, priority: int, value: object) -> None:
        """
        Initializes a new DSAHeapEntry with the given priority and value.

        Args:
            priority (int): The priority of the entry.
            value (object): The value associated with the entry.
        """
        self.priority = priority
        self.value = value

    def getPriority(self) -> int:
        """
        Get the priority of the DSAHeapEntry.

        Returns:
            int: The priority of the entry.
        """
        return self.priority

    def setPriority(self, priority: int) -> None:
        """
        Set the priority of the DSAHeapEntry.

        Args:
            priority (int): The new priority value to set.
        """
        self.priority = priority

    def getValue(self) -> object:
        """
        Get the value associated with the DSAHeapEntry.

        Returns:
            object: The value associated with the entry.
        """
        return self.value

    def setValue(self, value: object) -> None:
        """
        Set the value associated with the DSAHeapEntry.

        Args:
            value (object): The new value to associate with the entry.
        """
        self.value = value

if __name__ == "__main__":
    # Create some DSAHeapEntry objects
    entry1 = DSAHeapEntry(10, "Entry 1")
    entry2 = DSAHeapEntry(5, "Entry 2")
    entry3 = DSAHeapEntry(8, "Entry 3")

    # Print the initial entries
    print("Initial entries:")
    print(f"Entry 1: Priority={entry1.getPriority()}, Value='{entry1.getValue()}'")
    print(f"Entry 2: Priority={entry2.getPriority()}, Value='{entry2.getValue()}'")
    print(f"Entry 3: Priority={entry3.getPriority()}, Value='{entry3.getValue()}'")

    # Change the priority and value of entry1
    entry1.setPriority(7)
    entry1.setValue("Updated Entry 1")

    # Print the updated entry1
    print("\nUpdated Entry 1:")
    print(f"Entry 1: Priority={entry1.getPriority()}, Value='{entry1.getValue()}'")
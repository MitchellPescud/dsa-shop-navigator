# DSAHashTable.py - part of the shop navigator project
# Modified for shop navigation.

from HashDependencies.DSAHashEntry import DSAHashEntry
import numpy as np
import csv

class DSAHashTable:
    """
    A simple hash table implementation using a linear probing collision resolution scheme.
    """
    def __init__(self, tableSize: int) -> None:
        """
        Creates a new hash table with the given size.

        Args:
            tableSize: The size of the hash table.
        """
        self.count = 0
        self.actualSize = self._nextPrime(tableSize)
        self.hashArray = np.array([DSAHashEntry() for i in range(self.actualSize)])
        #print("Created hash array of size: " + str(self.hashArray.size))

    def put(self, key, value, resizeCheck: bool = False):
        """
        Inserts a new key-value pair into the hash table using double hashing for collision resolution.

        Args:
            key: The key to insert.
            value: The value to insert.
            resizeCheck: Whether to check for and resize the hash table if necessary.
        """
        if resizeCheck:
            self._check_and_resize(True)
        hash1 = self._hash(key)  # First hash using FNV
        hash2 = self._secondaryHash(key)  # Second hash using a different hash function

        # Initialize step size and initial hash value
        step = 1
        hashValue = hash1

        while self.hashArray[hashValue].getState() == 1:
            hashValue = (hash1 + step * hash2) % self.hashArray.size
            step += 1

        self.hashArray[hashValue] = DSAHashEntry(key, value)
        #print("Hash value for ", key, " created - ", hashValue)
        self.count += 1

    def get(self, key):
        """
        Gets the value associated with the given key in the hash table.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """

        hash_idx = self._hash(key)
        orig_idx = hash_idx
        found = False
        give_up = False

        while not found and not give_up:
            entry = self.hashArray[hash_idx]
            if entry.state == 0:
                give_up = True
            elif entry.key == key:
                found = True
            else:
                hash_idx = (hash_idx + 1) % self.hashArray.size
            if hash_idx == orig_idx:
                give_up = True

        if not found:
            raise KeyError(f"Key '{key}' not found in hash table.")

        return entry.value

    def remove(self, key):
        """
        Removes the key-value pair associated with the given key from the hash table.

        Args:
            key: The key to remove.
        """
        hashValue = self._hash(key)
        numIterations = 0  # Keep track of the number of iterations
        run = True
        
        while run == True:
            while numIterations < self.actualSize:
                if self.hashArray[hashValue].getState() == 0:
                    run = False
                if self.hashArray[hashValue].getKey() == key:
                    self.hashArray[hashValue] = DSAHashEntry()
                    self.hashArray[hashValue].setState(-1)
                    #print("Removing:", key, "-", hashValue)
                    self._check_and_resize(False, True)
                    return  # Key found and removed

                hashValue = (hashValue + 1) % self.hashArray.size
                numIterations += 1

        # If we reach this point, the key was not found in the table
        raise KeyError(f"Key '{key}' not found in hash table.")

    def getLoadFactor(self):
        """
        Calculates the load factor of the hash table.

        Returns:
            The load factor of the hash table.
        """
        loadFactor = self.count/(self.hashArray.size)
        return loadFactor

    def export(self, filename: str):
        """
        Exports the hash table to a CSV file.

        Args:
            filename: The name of the CSV file to export to.
        """
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Key", "Value"])
            for entry in self.hashArray:
                writer.writerow([entry.getKey(), entry.getValue()])

    def importFromCsv(self, filename: str):
        with open(filename, 'r') as csvFile:
            lines = csvFile.readlines()
            for line in lines:
                key, value = line.strip().split(',')
                self.put(key, value, True)

    def _resize(self, newSize):
        """
        Resizes the hash table to the given size.

        Args:
            newSize: The new size of the hash table.
        """
        # Store a reference to the old hash array
        oldHashArray = self.hashArray

        # Update the size of the hash table
        self.actualSize = self._nextPrime(newSize)
        self.count = 0  # Reset the count to 0 since we will reinsert all items

        # Create a new hash array with the new size
        self.hashArray = np.array([DSAHashEntry() for _ in range(newSize)])

        # Rehash and insert all existing key-value pairs from the old array
        for entry in oldHashArray:
            if entry.getState() == 1:
                self.put(entry.getKey(), entry.getValue())

        #print("Resized hash array to size:", self.actualSize)

    def _check_and_resize(self, upperOnly: bool = False, lowerOnly: bool = False) -> None:
        """
        Checks the load factor of the hash table and resizes if necessary.

        Args:
            upperOnly: Whether to only resize if the load factor is too high.
            lowerOnly: Whether to only resize if the load factor is too low.
        """
        # Calculate the current load factor
        loadFactor = self.getLoadFactor()

        if upperOnly == True:
            if loadFactor > 0.7:  # If the load factor is too high, triple the size
                #print("Resize required - loadfactor greater than 0.7! Resizing...")
                newSize = self.actualSize * 2
                self._resize(newSize)
        elif lowerOnly == True:
            if loadFactor < 0.2:  # If the load factor is too low, halve the size
                #print("Resize required - loadfactor less than 0.2! Resizing...")
                newSize = max(self.actualSize // 2, 10)  # Ensure a minimum size of 10
                self._resize(newSize)
        else:
            if loadFactor > 0.7:  # If the load factor is too high, triple the size
                #print("Resize required - loadfactor greater than 0.7! Resizing...")
                newSize = self.actualSize * 2
                self._resize(newSize)
            elif loadFactor < 0.2:  # If the load factor is too low, halve the size
                #print("Resize required - loadfactor less than 0.2! Resizing...")
                newSize = max(self.actualSize // 2, 10)  # Ensure a minimum size of 10
                self._resize(newSize)

    def _hash(self, key):
        """
        Hashes the given key to a hash index using FNV algorithm.

        Args:
            key: The key to hash.

        Returns:
            The hash index of the key.
        """
        FNVPrime = 16777619
        FNVOffset = 2166136261
        hashIdx = FNVOffset

        for char in key:
            hashIdx ^= ord(char)
            hashIdx *= FNVPrime

        return hashIdx % self.hashArray.size
    
    def _secondaryHash(self, key):
        """
        Calculate the secondary hash value using a different hash function.

        Args:
            key: The key to hash.

        Returns:
            The secondary hash index.
        """
        secondaryHash = 1  # Initialize with a non-zero value to avoid collisions
        for char in key:
            secondaryHash = (secondaryHash * 31 + ord(char)) % (self.hashArray.size - 1) + 1
        return secondaryHash

    def _nextPrime(self, startValue):
        """
        Finds the next prime number greater than or equal to the given value.

        Args:
            startValue: The starting value.

        Returns:
            The next prime number greater
        """
        if (startValue % 2 == 0):
            primeValue = startValue - 1
        else:
            primeValue = startValue
        isPrime = False
        while (not isPrime):
            primeValue += 2
            ii = 3
            isPrime = True
            rootValue = int(primeValue ** 0.5)
            while (ii <= rootValue) and (isPrime):
                if (primeValue % ii == 0):
                    isPrime = False
                else:
                    ii += 2
        return primeValue

if __name__ == "__main__":   
    # Create a hash table with an initial size of 10
    hash_table = DSAHashTable(1)

    # Insert key-value pairs into the hash table
    hash_table.put("apple", "red", True)
    hash_table.put("banana", "yellow", True)
    hash_table.put("cherry", "red", True)
    hash_table.put("date", "brown", True)
    hash_table.put("date1", "brown", True)
    hash_table.put("date2", "brown", True)
    hash_table.put("date3", "brown", True)
    hash_table.put("date4", "brown", True)
    hash_table.put("date5", "brown", True)
    hash_table.put("date6", "brown", True)
    hash_table.put("date7", "brown", True)
    hash_table.put("date8", "brown", True)
    hash_table.put("date9", "brown", True)



    # Retrieve values by their keys
    print("Value for 'apple':", hash_table.get("apple"))
    print("Value for 'banana':", hash_table.get("banana"))

    # Try to retrieve a value for a key that doesn't exist
    try:
        print("Value for 'grape':", hash_table.get("grape"))
    except KeyError as e:
        print(e)

    # Remove a key-value pair
    hash_table.remove("cherry")

    # Try to remove a key that doesn't exist
    try:
        print("Remove 'grape':", hash_table.remove("grape"))
    except KeyError as e:
        print(e)

    # Calculate and print the load factor
    loadFactor = hash_table.getLoadFactor()
    print("Load factor:", loadFactor)
    hash_table.export("test.csv")
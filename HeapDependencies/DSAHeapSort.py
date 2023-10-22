import numpy as np
from HeapDependencies.DSAHeapEntry import DSAHeapEntry
import csv

class DSAHeapSort:
    def __init__(self) -> None:
        """
        Initialize a DSAHeapSort instance.

        Attributes:
            heapArray (numpy.ndarray): An array to hold heap entries.
            heapArraySize (int): The size of the heapArray.
        """
        self.heapArray: np.ndarray
        self.heapArraySize: int

    def heapSort(self, array) -> np.ndarray:
        """
        Perform heap sort on an array.

        Args:
            array (list or numpy.ndarray): The input array to be sorted.

        Returns:
            numpy.ndarray: The sorted array.
        """
        self.heapArray = self._convertListOrArrayToHeapEntries(array)
        self.heapArraySize = self.heapArray.size

        # Build a max heap
        self._heapify(self.heapArray, self.heapArraySize)

        for i in range(self.heapArraySize - 1, 0, -1):
            # Swap the root (maximum element) with the last element of the heap
            self.heapArray[0], self.heapArray[i] = self.heapArray[i], self.heapArray[0]

            # Call trickleDown to maintain the max heap property on the reduced heap
            self._trickleDown(self.heapArray, 0, i)
    
    def heapSortFromCSV(self, csvFilename: str) -> np.ndarray:
        """
        Perform heap sort on data loaded from a CSV file.

        Args:
            csvFilename (str): The name of the CSV file to load data from and sort.

        Returns:
            numpy.ndarray: The sorted data as a NumPy array.
        """
        self.heapArray = self._importCsv(csvFilename)
        self.heapArraySize = self.heapArray.size

        # Build a max heap
        self._heapify(self.heapArray, self.heapArraySize)

        for i in range(self.heapArraySize - 1, 0, -1):
            # Swap the root (maximum element) with the last element of the heap
            self.heapArray[0], self.heapArray[i] = self.heapArray[i], self.heapArray[0]

            # Call trickleDown to maintain the max heap property on the reduced heap
            self._trickleDown(self.heapArray, 0, i)

    
    def displaySortedHeap(self):
        """
        Display the sorted heap.
        """
        for entry in self.heapArray:
            print(f"{entry.getValue()}")

    def exportToCSV(self, csvFilename: str):
        """
        Export the sorted heap to a CSV file.

        Args:
            csvFilename (str): The name of the CSV file to export to.
        """
        if self.heapArray is None:
            print("Heap is empty. Nothing to export.")
            return

        try:
            with open(csvFilename, 'w', newline='') as file:
                writer = csv.writer(file)
                for entry in self.heapArray:
                    writer.writerow([entry.getPriority(), entry.getValue()])
            print(f"Sorted heap exported to {csvFilename}.")
        except Exception as e:
            print(f"An error occurred while exporting to CSV: {e}")

    def getSortedHeap(self) -> np.ndarray:
        """
        Get the sorted heap as a NumPy array of DSAHeapEntry objects.

        Returns:
            numpy.ndarray: A NumPy array of DSAHeapEntry objects representing the sorted heap.
        """
        return self.heapArray

    def _convertListOrArrayToHeapEntries(self, inputListOrArray) -> np.ndarray:
        """
        Converts a Python list of tuples to a NumPy array of DSAHeapEntry objects.

        Args:
            inputListOrArray (list or numpy.ndarray): The input list of tuples, where each tuple contains (priority, value).

        Returns:
            numpy.ndarray: A NumPy array of DSAHeapEntry objects.
        """
        heapEntries = np.array([DSAHeapEntry(priority, value) for priority, value in inputListOrArray])
        return heapEntries

    def _importCsv(self, filename: str):
        """
        Import data from a CSV file.

        Args:
            filename (str): The name of the CSV file to import data from.

        Returns:
            numpy.ndarray: The imported data as a NumPy array.
        """
        try:
            data = None
            with open(filename, 'r') as file:
                for line in file:
                    # Split each line by a comma
                    row = line.strip().split(',')
                    
                    # Check the number of columns in the row
                    if len(row) != 2:
                        raise ValueError(f"Row {line.strip()} has {len(row)} columns, expected 2.")
                    
                    # Try to convert the first column to an integer
                    try:
                        firstColumn = int(row[0])
                    except ValueError:
                        print(f"Row {line.strip()} failed: First column is not an integer.")
                        continue
                    
                    # Create a NumPy array for the current row
                    rowArray = np.array([firstColumn, row[1]], dtype=object)
                    
                    # Stack the row array with existing data
                    if data is None:
                        data = rowArray
                    else:
                        data = np.vstack((data, rowArray))
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        heapEntries = self._convertListOrArrayToHeapEntries(data)
        print(f"Succefully imported {filename}.")
        return heapEntries

    def _heapify(self, heapArray, numItems):
        """
        Build a max heap from an array.

        Args:
            heapArray (numpy.ndarray): The array to build the max heap from.
            numItems (int): The number of items in the array.
        """
        for i in range((numItems // 2) - 1, -1, -1):
            self._trickleDown(heapArray, i, numItems)
    
    def _trickleDown(self, heapArray, index, numItems):
        """
        Perform trickle-down operation to maintain the max heap property.

        Args:
            heapArray (numpy.ndarray): The heap array.
            index (int): The index to start the trickle-down operation from.
            numItems (int): The number of items in the heap.
        """
        lChildIndex = 2 * index + 1
        rChildIndex = lChildIndex + 1
        keepTrickling = True

        while keepTrickling and lChildIndex < numItems:
            keepTrickling = False
            largeIndex = lChildIndex

            if rChildIndex < numItems and heapArray[lChildIndex].getPriority() > heapArray[rChildIndex].getPriority():
                largeIndex = rChildIndex

            if heapArray[largeIndex].getPriority() < heapArray[index].getPriority():
                heapArray[index], heapArray[largeIndex] = heapArray[largeIndex], heapArray[index]
                index = largeIndex
                lChildIndex = 2 * index + 1
                rChildIndex = lChildIndex + 1
                keepTrickling = True

# Example usage:
if __name__ == "__main__":
    
    # Perform heap sort
    sorted_entries = DSAHeapSort()
    sorted_entries.heapSortFromCSV("RandomNames7000.csv")
    sorted_entries.displaySortedHeap()
    sorted_entries.exportToCSV("SortedNames.csv")

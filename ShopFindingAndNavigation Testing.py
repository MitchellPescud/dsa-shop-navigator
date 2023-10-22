from ShopGraph import ShopGraph
from ShopEntry import Shop
from ShopHash import ShopFindingSystem
from HeapDependencies.DSAHeapSort import DSAHeapSort
import numpy as np

def getUserInput(inputType: str = "str", prompt: str = "Enter input: ", rangeCheck: bool = False, lowerLimit: float = None, upperLimit: float = None) -> (str | int | float):
    """
    Get user input of the specified type with optional range checks.

    Args:
        inputType (str): The expected input type ('str', 'int', or 'float').
        prompt (str): The prompt message for the user.
        rangeCheck (bool): If True, check if the input is within the specified range.
        lowerLimit (float): The lower limit for the input (if rangeCheck is True).
        upperLimit (float): The upper limit for the input (if rangeCheck is True).

    Returns:
        str | int | float: The user input of the specified type.

    Raises:
        ValueError: If the input is not of the expected type.
    """
    while True:
        userInput = input(prompt)
        if userInput.strip():  # Check if the input is not empty after stripping whitespace
            if inputType == "str":
                return userInput
            elif inputType == "int":
                try:
                    userInput = int(userInput)
                    if rangeCheck:
                        if lowerLimit is not None and upperLimit is not None:
                            if lowerLimit <= userInput <= upperLimit:
                                return userInput
                            else:
                                print(f"Input must be between {lowerLimit} and {upperLimit}. Please try again.")
                        elif lowerLimit is not None:
                            if lowerLimit <= userInput:
                                return userInput
                            else:
                                print(f"Input must be greater than or equal to {lowerLimit}. Please try again.")
                        elif upperLimit is not None:
                            if userInput <= upperLimit:
                                return userInput
                            else:
                                print(f"Input must be less than or equal to {upperLimit}. Please try again.")
                    else:
                        return userInput
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            elif inputType == "float":
                try:
                    userInput = float(userInput)
                    if rangeCheck:
                        if lowerLimit is not None and upperLimit is not None:
                            if lowerLimit <= userInput <= upperLimit:
                                return userInput
                            else:
                                print(f"Input must be between {lowerLimit} and {upperLimit}. Please try again.")
                        elif lowerLimit is not None:
                            if lowerLimit <= userInput:
                                return userInput
                            else:
                                print(f"Input must be greater than or equal to {lowerLimit}. Please try again.")
                        elif upperLimit is not None:
                            if userInput <= upperLimit:
                                return userInput
                            else:
                                print(f"Input must be less than or equal to {upperLimit}. Please try again.")
                    else:
                        return userInput
                except ValueError:
                    print("Invalid input. Please enter a float.")
        else:
            print("Input cannot be blank. Please try again.")
    
def createShop() -> Shop:
    """
    Create a new shop by collecting information from the user and return it as a Shop object.

    Returns:
        Shop: A new Shop object with user-provided information.
    """
    shopNum = getUserInput("int", "Enter Shop Number: ", True, 1)
    shopName = getUserInput("str", "Enter Shop Name: ")
    shopCategory = getUserInput("str", "Enter Shop Category: ")
    shopLocation = getUserInput("str", "Enter Shop Location: ")
    shopRating = getUserInput("float", "Enter Shop Rating: ", True, 0, 5)
    return Shop(shopNum, shopName, shopCategory, shopLocation, shopRating)

def modifyShop(modifier: int, originalShopInfo: Shop) -> None:
    """
    Modify specific attributes of a shop based on the modifier choice.

    Args:
        modifier (int): An integer representing the attribute to be modified (1 for Shop Number, 2 for Name, etc.).
        originalShopInfo (Shop): The original Shop object to be modified.

    Returns:
        None
    """
    if modifier == 1:
        print(f"Current Shop Number: {originalShopInfo.getNum()}")
        newNum = getUserInput("int", "Enter New Shop Number: ", True, 1)
        originalShopInfo.setNum(newNum)
    elif modifier == 2:
        print(f"Current Shop Name: {originalShopInfo.getName()}")
        newName = getUserInput("str", "Enter New Shop Name: ")
        originalShopInfo.setName(newName)
    elif modifier == 3:
        print(f"Current Shop Category: {originalShopInfo.getCategory()}")
        newCategory = getUserInput("str", "Enter New Shop Category: ")
        originalShopInfo.setCategory(newCategory)
    elif modifier == 4:
        print(f"Current Shop Location: {originalShopInfo.getLocation()}")
        newLocation = getUserInput("str", "Enter New Shop Location: ")
        originalShopInfo.setLocation(newLocation)
    elif modifier == 5:
        print(f"Current Shop Rating: {originalShopInfo.getRating()}")
        newRating = getUserInput("float", "Enter New Shop Rating: ", True, 0, 5)
        originalShopInfo.setRating(newRating)

def main():
    """
    The main function that provides a menu-driven interface for interacting with a shop management system.
    """
    run = True
    shopGraph = ShopGraph()
    shopHashTable = ShopFindingSystem()
    shopCategorySort = DSAHeapSort()

    print("ShopFindingAndNavigation Testing Version")
    while run == True:
        print("\nOptions:")
        print("1.  Add Shops")
        print("2.  Add Paths between Shops")
        print("3.  Edit Shop Information")
        print("4.  Delete Shop")
        print("5.  Delete Path")
        print("6.  Display ShopGraph (List)")
        print("7.  Display ShopGraph (Matrix)")
        print("8.  Get Shop Directions (Graph Traversal)")
        print("9.  Search Shops By Category")
        print("10. Export Shop Hash Table")
        print("11. Quit")

        choice = getUserInput("int", "Enter your choice: ", True, 1, 11)  # Get the user's choice as an integer

        if choice == 1:   #Add Shops
            # Create 10 different shop objects
            shop1 = Shop(12, "ABC Electronics", "Electronics", "Floor 1, Aisle 3", 4.0)
            shop2 = Shop(27, "Fashion Paradise", "Clothing", "Floor 2, Aisle 1", 5.0)
            shop3 = Shop(32, "XYZGadgets", "Electronics", "Floor 2, Aisle 3", 5.0)
            shop4 = Shop(41, "TechHub", "Electronics", "Floor 3, Aisle 2", 4.5)
            shop5 = Shop(59, "Shoe Stop", "Footwear", "Floor 1, Aisle 2", 4.2)
            shop6 = Shop(65, "Book Nook", "Books", "Floor 3, Aisle 1", 4.7)
            shop7 = Shop(73, "Fresh Mart", "Groceries", "Floor 1, Aisle 4", 4.8)
            shop8 = Shop(80, "Sports Zone", "Sports Equipment", "Floor 2, Aisle 2", 4.3)
            shop9 = Shop(91, "Jewelry Palace", "Jewelry", "Floor 3, Aisle 4", 4.9)
            shop10 = Shop(17, "Home Decor Haven", "Home Decor", "Floor 1, Aisle 1", 4.6)
            shopGraph.addShop("ABCE", shop1)
            shopGraph.addShop("FP", shop2)
            shopGraph.addShop("XYZG", shop3)
            shopGraph.addShop("TH", shop4)
            shopGraph.addShop("SS", shop5)
            shopGraph.addShop("BN", shop6)
            shopGraph.addShop("FM", shop7)
            shopGraph.addShop("SZ", shop8)
            shopGraph.addShop("JP", shop9)
            shopGraph.addShop("HDH", shop10)
            shopHashTable.addShop(shop1)
            shopHashTable.addShop(shop2)
            shopHashTable.addShop(shop3)
            shopHashTable.addShop(shop4)
            shopHashTable.addShop(shop5)
            shopHashTable.addShop(shop6)
            shopHashTable.addShop(shop7)
            shopHashTable.addShop(shop8)
            shopHashTable.addShop(shop9)
            shopHashTable.addShop(shop10)

        elif choice == 2: #Add a Path between Shops
            try:
                shopGraph.addPath("1", "2", "1 to 2", 3)
                shopGraph.addPath("2", "4", "2 to 4", 5)
                shopGraph.addPath("3", "2", "3 to 2", 1)
                shopGraph.addPath("5", "6", "5 to 6", 6)
                shopGraph.addPath("4", "5", "4 to 5", 8)
                shopGraph.addPath("3", "9", "3 to 9", 3)
                shopGraph.addPath("9", "8", "9 to 8", 4)
                shopGraph.addPath("8", "7", "8 to 7", 6)
                shopGraph.addPath("10", "1", "10 to 1", 7)
                shopGraph.addPath("10", "7", "10 to 7", 4)
                shopGraph.addPath("8", "2", "8 to 2", 9)
            except ValueError as e:
                print(e)

        elif choice == 3: #Edit Shop Information
            edit = True
            shopToEdit = getUserInput("str", "Enter the unique shop ID to edit: ")
            while edit == True:
                try:
                    shopNodeToModify = shopGraph.getShop(shopToEdit)
                    originalShopInfo = shopNodeToModify.getValue()
                    shopHashTable.removeShop(originalShopInfo)
                    print(f"Current Shop Information: \n{originalShopInfo}")
                    print("Modification Options:")
                    print("1. Shop Number")
                    print("2. Name")
                    print("3. Category")
                    print("4. Location")
                    print("5. Rating")
                    modificationChoice = getUserInput("int", "Please select the value you wish to modify: ", True, 1, 5)  # Get the user's choice as an integer
                    modifyShop(modificationChoice, originalShopInfo, shopHashTable)
                    continueChoice = getUserInput("int", "Would you like to continue\t(1) - Yes\t(2) - No:", True, 1, 2)  # Get the user's choice as an integer
                    if continueChoice == 2:
                        shopHashTable.addShop(originalShopInfo)
                        edit = False
                except ValueError as e:
                    print(e)
                    edit = False

        elif choice == 4: #Delete Shop
            shopIDToDelete = getUserInput("str", "Enter the unique shop ID to delete: ")
            try:
                shopToDelete =  shopGraph.getShop(shopIDToDelete)
                shopInfo = shopToDelete.getValue()
                shopGraph.deleteShop(shopIDToDelete)
                shopHashTable.removeShop(shopInfo)
                print(f"Shop {shopIDToDelete} deleted!")
            except ValueError as e:
                print(e)

        elif choice == 5: #Delete Path
            sourceShop = getUserInput("str", "Enter the source shop ID: ")
            targetShop = getUserInput("str", "Enter the target shop ID: ")
            try:
                shopGraph.deletePath(sourceShop, targetShop)
                print(f"Path from {sourceShop} to {targetShop} deleted!")
            except ValueError as e:
                print(e)

        elif choice == 6: #Display ShopGraph (List)
            try:
                print("ShopGraph (List):")
                shopGraph.displayGraphList()
            except RuntimeError as e:
                print(e)

        elif choice == 7: #Display ShopGraph (Matrix)
            try:
                print("ShopGraph (Matrix):")
                shopGraph.displayGraphMatrix()
            except RuntimeError as e:
                print(e)

        elif choice == 8: #Get Shop Directions (Graph Traversal)
            sourceShop = getUserInput("str", "Enter the starting shop ID: ")
            targetShop = getUserInput("str", "Enter the target shop ID: ")
            try:
                DFSResult = shopGraph.depthFirstSearch(sourceShop, targetShop, True)
                DFSResult.display("Depth First Search - Path: ")
                BFSResult = shopGraph.breadthFirstSearch(sourceShop, targetShop, True)
                BFSResult.display("Breadth First Search - Path: ")
                DFSSize = DFSResult.size()
                BFSSize = BFSResult.size()
                if DFSSize == BFSSize:
                    print(f"Both paths are same length of {DFSSize} shops apart, please choose one of the above routes.")
                elif DFSSize < BFSSize:
                    print(f"Depth First Search resulted in the shortest path of {DFSSize} shops apart, please follow the below route")
                    DFSResult.display("Path: ")
                else:
                    print(f"Breadth First Search resulted in the shortest path of {BFSSize} shops apart, please follow the below route")
                    BFSResult.display("Path: ")    
            except ValueError as e:
                print(e)
            except RuntimeError as e:
                print(e)

        elif choice == 9: #Search Shops By Category
            category = getUserInput("str", "Enter category to find shops: ")
            
            try:
                shops = shopHashTable.searchByCategory(category)
                sort = getUserInput("int", "Would you like to sort shops by highest to lowest rating (1. Yes or 2. No): ", True, 1,2)
                if sort == 2:
                    shops.display("Results:\n","\n")
                elif sort == 1:
                    shopArray = shops.toNumpyArray()
                    dtype = [('rating', float), ('shop', object)]
                    preHeapArray = np.empty(len(shopArray), dtype=dtype)
                    # Loop through each shop in shopArray to get the rating and populate newArray
                    for i, shop in enumerate(shopArray):
                        shopRating = shop.getRating()  # Replace with your actual method call
                        preHeapArray[i] = (shopRating, shop)
                    shopCategorySort.heapSort(preHeapArray)
                    shopCategorySort.displaySortedHeap()
            except KeyError:
                print(f"No shops found in category - {category}")

        elif choice == 10: #Export Shop Hash Table
            shopHashTable.shopCategories.export("ShopNavHashTable.csv")
            
        elif choice == 11: #Quit
            run = False

if __name__ == '__main__':
    main()

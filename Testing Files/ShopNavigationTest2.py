from ShopGraph import ShopGraph
from ShopEntry import Shop

def getUserInput(inputType: str = "str", prompt: str = "Enter input: ", rangeCheck: bool = False, lowerLimit: float = None, upperLimit: float = None) -> (str | int | float):
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

    shopNum = getUserInput("int", "Enter Shop Number: ", True, 1)
    shopName = getUserInput("str", "Enter Shop Name: ")
    shopCategory = getUserInput("str", "Enter Shop Category: ")
    shopLocation = getUserInput("str", "Enter Shop Location: ")
    shopRating = getUserInput("float", "Enter Shop Rating: ", True, 0, 5)

    
    return Shop(shopNum, shopName, shopCategory, shopLocation, shopRating)

def modifyShop(modifier: int, originalShopInfo: Shop) -> None:
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
    run = True
    shopGraph = ShopGraph()

    while run == True:
        print("\nOptions:")
        print("1. Add a Shop")
        print("2. Add a Path between Shops")
        print("3. Edit Shop Information")
        print("4. Delete Shop")
        print("5. Delete Path")
        print("6. Display ShopGraph (List)")
        print("7. Display ShopGraph (Matrix)")
        print("8. Get Shop Directions (Graph Traversal)")
        print("9. Quit")

        choice = getUserInput("int", "Enter your choice: ", True, 1, 8)  # Get the user's choice as an integer

        if choice == 1:   #Add a Shop
            shop = createShop()
            shopID = getUserInput("str", "Enter a unique ID for the shop: ")
            shopGraph.addShop(shopID, shop)

        elif choice == 2: #Add a Path between Shops
            sourceShop = getUserInput("str", "Enter the source shop ID: ")
            targetShop = getUserInput("str", "Enter the target shop ID: ")
            pathName = getUserInput("str", "Enter the path name: ")
            pathDistance = getUserInput("int", "Enter the distance between shops: ", True, 0)

            try:
                shopGraph.addPath(sourceShop, targetShop, pathName, pathDistance)
            except ValueError as e:
                print(e)

        elif choice == 3: #Edit Shop Information
            edit = True
            shopToEdit = getUserInput("str", "Enter the unique shop ID to edit: ")
            while edit == True:
                try:
                    shopNodeToModify = shopGraph.getShop(shopToEdit)
                    originalShopInfo = shopNodeToModify.getValue()
                    print(f"Current Shop Information: \n{originalShopInfo}")
                    print("Modification Options:")
                    print("1. Shop Number")
                    print("2. Name")
                    print("3. Category")
                    print("4. Location")
                    print("5. Rating")
                    modificationChoice = getUserInput("int", "Please select the value you wish to modify: ", True, 1, 5)  # Get the user's choice as an integer
                    modifyShop(modificationChoice, originalShopInfo)
                    continueChoice = getUserInput("int", "Would you like to continue\t(1) - Yes\t(2) - No:", True, 1, 2)  # Get the user's choice as an integer
                    if continueChoice == 2:
                        edit = False
                except ValueError as e:
                    print(e)
                    edit = False

        elif choice == 4: #Delete Shop
            shopToDelete = getUserInput("str", "Enter the unique shop ID to delete: ")
            try:
                shopGraph.deleteShop(shopToDelete)
                print(f"Shop {shopToDelete} deleted!")
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
            
        elif choice == 9: #Quit
            run = False

if __name__ == '__main__':
    main()

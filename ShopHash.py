from HashDependencies.DSAHashTable import DSAHashTable
from ShopEntry import Shop
from GraphDependencies.DSALinkedLists import DSALinkedList

class ShopFindingSystem:
    def __init__(self):
        """
        Initialize a ShopFindingSystem instance.

        This class manages a hash table of shops grouped by their categories.

        Attributes:
            shopCategories (DSAHashTable): A hash table for categorizing shops.
        """
        # Initialize a hash table for shop categories
        self.shopCategories = DSAHashTable(2)

    def addShop(self, shop: Shop):
        """
        Add a shop to the shop finding system.

        Args:
            shop (Shop): The shop to be added to the system.

        Returns:
            None
        """
        # Retrieve the list of shops in the specified category (or create a new list if not present)
        category = shop.category
        try:
            shops = self.shopCategories.get(category)
            self.shopCategories.remove(category)
        except KeyError:
            shops = DSALinkedList()
        
        # Append the new shop to the list
        shops.insertLast(shop)

        
        # Update the hash table with the updated list of shops
        self.shopCategories.put(category, shops, resizeCheck=True)

    def searchByCategory(self, category) -> DSALinkedList:
        """
        Search for shops by a specified category.

        Args:
            category (str): The category to search for.

        Returns:
            DSALinkedList: A linked list of shops in the specified category.
        """
        # Retrieve the list of shops in the specified category
        shops = self.shopCategories.get(category)
        return shops

    def removeShop(self, shop: Shop):
        """
        Remove a shop from the shop finding system.

        Args:
            shop (Shop): The shop to be removed from the system.

        Returns:
            None
        """
        category = shop.category
        try:
            # Retrieve the list of shops in the specified category
            shops = self.shopCategories.get(category)

            if isinstance(shops, DSALinkedList):
                # Remove the shop from the list
                shops.remove(shop)
                if shops.isEmpty():
                    # Remove category
                    self.shopCategories.remove(category)
                else:
                    # Update the hash table with the updated list of shops
                    self.shopCategories.remove(category)
                    self.shopCategories.put(category, shops)
        except KeyError:
            print("No shop found with that information!")


if __name__ == '__main__':
    # Sample usage:
    shopSystem = ShopFindingSystem()
    shop1 = Shop(1, "ABC", "Electronics", "Floor 1, Aisle 3", 4)
    shop2 = Shop(2, "Fashion Paradise", "Clothing", "Floor 2, Aisle 1", 5)
    shop3 = Shop(3, "XYZGadgets", "Electronics", "Floor 2, Aisle 3", 5)

    shopSystem.addShop(shop1)
    shopSystem.addShop(shop2)
    shopSystem.addShop(shop3)
    shopSystem.shopCategories.export("test.csv")
    

    # Add 10 more shops with "Electronics" category
    for i in range(4, 30):
        shop = Shop(i, f"Shop {chr(ord('A') + i - 4)}", "Electronics", "Floor 1", 4.2)
        shopSystem.addShop(shop)
        print(f"Shop {chr(ord('A') + i - 4)} added successfully.")

    # Search for shops in the "Electronics" category
    electronicShops = shopSystem.searchByCategory("Electronics")
    if electronicShops:
        electronicShops.display("","\n")
    else:
        print("No matching shops found in the 'Electronics' category.")

    shopSystem.removeShop(shop3)

    # Add 10 more shops with "Electronics" category
    for i in range(31, 36):
        shop = Shop(i, f"Shop {chr(ord('A') + i - 4)}", "Tech", "Floor 2", 4.2)
        shopSystem.addShop(shop)
        print(f"Shop {chr(ord('A') + i - 4)} added successfully.")
    
    # Search for shops in the "Electronics" category
    electronicShops = shopSystem.searchByCategory("Electronics")
    if electronicShops:
        electronicShops.display("","\n")
    else:
        print("No matching shops found in the 'Electronics' category.")

    # Search for shops in the "Electronics" category
    electronicShops = shopSystem.searchByCategory("Tech")
    if electronicShops:
        electronicShops.display("","\n")
    else:
        print("No matching shops found in the 'Electronics' category.")

from HashDependencies.DSAHashTable import DSAHashTable
from ShopEntry import Shop

def main():
    table_size = 10  # Initial size of the hash table
    shop_table = DSAHashTable(table_size)

    shop_A = Shop(1, "Shop A", "Electronics", "Floor 1", 4.5)
    shop_B = Shop(2, "Shop B", "Electronics", "Floor 1", 4.0)
    shop_C = Shop(3, "Shop C", "Electronics", "Floor 1", 4.8)

    shop_table.put(shop_A.getCategory(), shop_A, resizeCheck=True)
    print("Shop A added successfully.")

    shop_table.put(shop_B.getCategory(), shop_B, resizeCheck=True)
    print("Shop B added successfully.")

    shop_table.put(shop_C.getCategory(), shop_C, resizeCheck=True)
    print("Shop C added successfully.")

    # Add 10 more shops with "Electronics" category
    for i in range(4, 30):
        shop = Shop(i, f"Shop {chr(ord('A') + i - 4)}", "Electronics", "Floor 1", 4.2)
        shop_table.put(shop.getCategory(), shop, resizeCheck=True)
        print(f"Shop {chr(ord('A') + i - 4)} added successfully.")

    try:
        shop_table.export("test.csv")
        print(f"Shop data exported to test.csv")
    except Exception as e:
        print(f"An error occurred: {e}")

main()

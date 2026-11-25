# Shop Navigator

A command-line tool for managing a shopping centre and finding your way around it, built on **hand-written data structures** (no built-in collections doing the heavy lifting).

| Feature | Data structure |
|---|---|
| Shops and the paths between them | Weighted **graph** (list and matrix views) |
| Directions between shops | **Graph traversal** with a custom stack and queue |
| Search shops by category | **Hash table** (with CSV export) |
| Ranking shops | **Heap** and heap sort |

The supporting structures (`DSALinkedLists`, `DSAstack`, `DSAqueues`, `DSAHashTable`, `DSAHeap`, ...) live in the `*Dependencies/` folders.

## Run
Requires Python 3.10+ and NumPy.
```bash
pip install -r requirements.txt
python ShopFindingAndNavigation.py
```
Menu: add / edit / delete shops and paths, display the graph as a list or matrix, get directions, search by category, export the hash table.

## Project layout
- `ShopEntry.py` – `Shop` class (number, name, category, location, rating)
- `ShopGraph.py` – graph and traversal
- `ShopHash.py` – hash-table category search
- `ShopFindingAndNavigation.py` – interactive menu
- `Testing Files/` – interactive test drivers (`ShopNavigationTest2-5.py`) with their own dependency copies; run them from inside that folder

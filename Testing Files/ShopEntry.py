class Shop:
    """
    A class to represent a shop.

    Attributes:
        num (int): The shop's unique number.
        name (str): The name of the shop.
        category (str): The category or type of the shop.
        location (str): The location of the shop.
        rating (float): The rating of the shop.
    """

    def __init__(self, number: int, name: str, category: str, location: str, rating: float) -> None:
        """
        Initialize a new Shop object.

        Args:
            number (int): The unique number of the shop.
            name (str): The name of the shop.
            category (str): The category or type of the shop.
            location (str): The location of the shop.
            rating (float): The rating of the shop.
        """
        self.num = number
        self.name = name
        self.category = category
        self.location = location
        self.rating = rating

    def __str__(self) -> str:
        """
        Return a string representation of the shop's attributes.

        Returns:
            str: A string with all attributes.
        """
        return f"Shop Number: {self.num}\tName: {self.name}\tCategory: {self.category}\tLocation: {self.location}\tRating: {self.rating}"

    def getNum(self) -> int:
        """
        Get the unique number of the shop.

        Returns:
            int: The shop's unique number.
        """
        return self.num

    def setNum(self, number: int) -> None:
        """
        Set the unique number of the shop.

        Args:
            number (int): The new unique number for the shop.

        Returns:
            None
        """
        self.num = number

    def getName(self) -> str:
        """
        Get the name of the shop.

        Returns:
            str: The name of the shop.
        """
        return self.name

    def setName(self, name: str) -> None:
        """
        Set the name of the shop.

        Args:
            name (str): The new name for the shop.

        Returns:
            None
        """
        self.name = name

    def getCategory(self) -> str:
        """
        Get the category of the shop.

        Returns:
            str: The category or type of the shop.
        """
        return self.category

    def setCategory(self, category: str) -> None:
        """
        Set the category of the shop.

        Args:
            category (str): The new category for the shop.

        Returns:
            None
        """
        self.category = category

    def getLocation(self) -> str:
        """
        Get the location of the shop.

        Returns:
            str: The location of the shop.
        """
        return self.location

    def setLocation(self, location: str) -> None:
        """
        Set the location of the shop.

        Args:
            location (str): The new location for the shop.

        Returns:
            None
        """
        self.location = location

    def getRating(self) -> float:
        """
        Get the rating of the shop.

        Returns:
            float: The rating of the shop.
        """
        return self.rating

    def setRating(self, rating: float) -> None:
        """
        Set the rating of the shop.

        Args:
            rating (float): The new rating for the shop.

        Returns:
            None
        """
        self.rating = rating

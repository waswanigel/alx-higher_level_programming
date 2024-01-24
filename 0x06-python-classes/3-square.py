#!/usr/bin/python3
# 3-square.py

"""a class that defines a Square."""

class Square:
    """defines a square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): The size of the initialised square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Return the current area of the square."""
            return (self.__size * self.__size)

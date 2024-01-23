#!/usr/bin/python3
# 2-square.py

"""a class that defines a Square."""

class Square:
    """defines a square."""
    def __init__(self, size):
        """Initialize a Square.
        Args:
        size (int): The size of the initialised square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size 

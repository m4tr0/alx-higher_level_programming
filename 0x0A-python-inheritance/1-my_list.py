#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """
    Custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

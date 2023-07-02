#!/usr/bin/python3
"""
This module provides a function for indenting text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char

        if char in special_chars:
            current_line = current_line.strip()
            lines.append(current_line)
            lines.append("")
            current_line = ""

    current_line = current_line.strip()
    lines.append(current_line)

    for line in lines:
        print(line)

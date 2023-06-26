#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end=" ")  # Print the element
            count += 1
    except IndexError:
        pass  # Ignore IndexError when the list is exhausted

    print()  # Print a new line
    return count

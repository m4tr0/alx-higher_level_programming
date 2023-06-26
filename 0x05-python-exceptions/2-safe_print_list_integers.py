#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for element in my_list[:x]:
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                count += 1
        print()

    except TypeError:
        print("An exception occurred. The list doesn't have enough elements.")

    return count

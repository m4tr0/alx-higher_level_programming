#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Convert the list to a set to get unique elements
    sum_unique = sum(unique_numbers)  # Calculate the sum of unique elements
    return sum_unique

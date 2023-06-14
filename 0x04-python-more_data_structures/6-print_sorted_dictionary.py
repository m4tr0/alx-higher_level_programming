def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())  # Get the sorted keys of the dictionary

    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")

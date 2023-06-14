def only_diff_elements(set_1, set_2):
    diff_elements = set_1.symmetric_difference(set_2)  # Use the symmetric_difference method to find elements present in only one set
    return diff_elements

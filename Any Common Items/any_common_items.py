list1 = ["a", "b", "c", "x"]
list2 = ["z", "y", "i"]
list3 = ["z", "y", "x"]

def any_common_elements(first_list, second_list):

    unique_chars = set()
    for element in first_list:
        unique_chars.add(element)
    for element in second_list:
        if element in unique_chars:
            return True
    return False

    """
    freqs = {}
    for elem in first_list:
        if elem not in freqs:
            freqs[elem] = None
    for elem in second_list:
        if elem in freqs:
            return True
    return False
    """

print(any_common_elements(list1, list2))
print(any_common_elements(list1, list3))

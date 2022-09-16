#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max_value = my_list[0]
    # Now traverse through the list and compare
    for x in my_list:
        # each number with "max" value. Whichever is
        # largest assign that value to "max'.
        if x > max_value:
            max_value = x
    return max_value

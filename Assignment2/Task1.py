# Task 1
def distinct_generator(target_list, processed_list):
    for x in processed_list:                          # Go through all values of given list.
        if x not in target_list:                      # Return each value if it is not inside target list already.
            yield x

def distinct(list):
    result_list = []                                  # Create list that will accept distinct elements.
    for x in distinct_generator(result_list, list):   # Create cycle with generator, pass created ealrier list and given list as arguments.
        result_list.append(x)                         # Now, result_list will accept elements, and this changes are visible in generator,
    return result_list                                # meaning generator can look if value is not inside the list and don't yield it in such case.

# Demonstration
lst = ["a", "a", "b", "c", "d", "e", "e", "e"]
print(distinct(lst)) # Expected: ['a', 'b', 'c', 'd', 'e']
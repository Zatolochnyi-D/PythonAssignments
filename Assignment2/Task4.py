# Task 4
def combine_lists(*lists):
    return [el for list in lists for el in list]  # For each list for each it's element return element.

# Demonstration
lst1 = ['a', 'b']
lst2 = ['c', 'd']
lst3 = ['e', 'f']
print(combine_lists(lst1, lst2, lst3)) # Expected: ['a', 'b', 'c', 'd', 'e', 'f']
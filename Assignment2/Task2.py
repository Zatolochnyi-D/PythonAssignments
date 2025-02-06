# Task 2
def enumerate_into_dict(list):                      # Just iterate through indices and create dict, where keys are indices and values are values in list
    return {i: list[i] for i in range(len(list))}   # under this indices.

# Demonstration
lst = ["a", "b", "d", "c"]
print(enumerate_into_dict(lst)) # Expected: {0: 'a', 1: 'b', 2: 'd', 3: 'c'}
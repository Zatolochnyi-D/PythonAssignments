# Task 2
def select_even(list):
    return [x for x in list if x % 2 == 0]

# Demonstration
print(select_even([1, 2, 3, 4, 5, 6, 7, 8])) # Expected: [2, 4, 6, 8]
# Task 3                                                              # Iterate through indices and get all the list elements, which idices are
def get_range(list, start, end):                                      # inside of range [start; end]. Range being outside of list bounds is insignificant,
    return [list[i] for i in range(len(list)) if start <= i <= end]   # as generator only selects indices only inside list's bounds.
                                                                      
# Demonstration
lst = ["a", "b", "c", "d", "e", "f"]
print(get_range(lst, 2, 4)) # Expected: ['c', 'd', 'e']
print(get_range(lst, 4, 9)) # Expected: ['e', 'f']
print(get_range(lst, 5, 5)) # Expected: ['f']
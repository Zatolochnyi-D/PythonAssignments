# Task 1
from random import randint as r
def generate_random_list(length):
    return [r(0, 100) for x in range(length)]

# Demonstration
print(generate_random_list(5)) # Expected: [N, N, N, N, N], where N - random integer in range [0; 100]]


# Task 2
def select_even(list):
    return [x for x in list if x % 2 == 0]

# Demonstration
print(select_even([1, 2, 3, 4, 5, 6, 7, 8])) # Expected: [2, 4, 6, 8]


# Task 3                                                              # Iterate through indices and get all the list elements, which idices are
def get_range(list, start, end):                                      # inside of range [start; end]. Range being outside of list bounds is insignificant,
    return [list[i] for i in range(len(list)) if start <= i <= end]   # as generator only selects indices only inside list's bounds.
                                                                      
# Demonstration
lst = ["a", "b", "c", "d", "e", "f"]
print(get_range(lst, 2, 4)) # Expected: ['c', 'd', 'e']
print(get_range(lst, 4, 9)) # Expected: ['e', 'f']
print(get_range(lst, 5, 5)) # Expected: ['f']


# Task 4
def select_odds_in_range(begin, end):
    return [x for x in range(begin, end + 1) if x % 2 == 1]

# Demonstration
print(select_odds_in_range(3, 9)) # Expected: [3, 5, 7, 9]


# Task 5
def infinite(lst, tries):
    for i in range(tries):
        yield lst[i % len(lst)]

# Demonstration
for el in infinite([1, 2, 3, 4], 7):    # Expected: 1 2 3 4 1 2 3
    print(el, end=' ')
print()
# Task 5
def infinite(lst, tries):
    for i in range(tries):
        yield lst[i % len(lst)]

# Demonstration
for el in infinite([1, 2, 3, 4], 7):    # Expected: 1 2 3 4 1 2 3
    print(el, end=' ')
print()
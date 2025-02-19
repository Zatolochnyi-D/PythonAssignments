# Task 2
def len_of_string(string):
    counter = 0
    for letter in string:    # Just increase counter per each iterated symbol.
        counter += 1
    return counter

# Demonstration

print(len_of_string("abcde")) # Expected : 5
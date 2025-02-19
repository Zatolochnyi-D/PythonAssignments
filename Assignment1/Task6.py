# Task 6
def sum_strings(list):
    result = 0.0
    for el in list:
        result += float(el)
    return result

# Demonstration
print(sum_strings(["100", "0.5", "-58.5"])) # Expected: 42.0
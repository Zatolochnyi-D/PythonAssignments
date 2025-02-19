# Taks 1
def find_matches(string1, string2):
    combinations1 = []
    for i in range(1, len(string1)):
        combinations1.append(string1[i-1] + string1[i])    # Read every combination of 2 letters from first string.
    combinations2 = []
    for i in range(1, len(string2)):
        combinations2.append(string2[i-1] + string2[i])    # Read every combination of 2 letters from second string.
    result = []
    for combination in combinations1:                      # Select every combination that is in both combination lists.
        if (combination in combinations2):
            result.append(combination)
    return len(result)

# Demonstration
print(find_matches("akkad", "drakkar")) # Expected: 3
# Task 4
def replace_symbols(string_list, symbol):
    for string in string_list:              # Stop function if there are words with size less than 3.
        if (len(string) < 3):
            return None
    result_list = []
    for string in string_list:
        result = string[:-2]                # For each word in given list, get substring from 0 to 3-from-end symbol.
        result += symbol * 3                # Add to substring given symbol 3 times.
        result_list.append(result)
    return result_list

# Demonstration
print(replace_symbols(["abcde", "string", "Task4"], "%")) # Expected: ['ab%%%', 'str%%%', 'Ta%%%']
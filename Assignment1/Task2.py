# Program
def combine_dicts(dicts):
    keys = set()                                    # Set to collect distinct keys.
    for dict in dicts:                              # Go through all given dicts.
        for key in dict.keys():                     # Go through keys of each dict.
            keys.add(key)                           # Add key to set (and it's discarded if there is already the same key inside).

    result_dict = {}                                
    for key in keys:                                # Go through all the keys.
        result_dict[key] = []                       # Create list under key in resulting dict.
        for dict in dicts:                          # Go through all gicen dicts.
            try:                                    # Add to created ealrier list value under the same key in each dict.
                result_dict[key].append(dict[key])
            except KeyError:                        # If dict does not have such key, skip.
                continue

    return result_dict

# Demonstration
dicts = [
    {
        "a": "letter",
        "b": "letter",
        "c": "letter",
    },
    {
        "b": "letter",
        "d": "letter",
        "1": "number",
    },
    {
        "c": "letter",
        "1": "number",
        "2": "number",
    },
]
print(combine_dicts(dicts)) # Expected (in any order): {'1': ['number', 'number'], '2': ['number'], 'b': ['letter', 'letter'], 'd': ['letter'], 'c': ['letter', 'letter'], 'a': ['letter']}
# Task 2
def combine_dicts(dicts):
    # Collect keys of each dict into set to get only unique ones.
    keys = set()
    for dict in dicts:
        for key in dict.keys():
            keys.add(key)

    # Create resulting dict by using keys set values as keys and list of corresponding to keys values in dicts as values.
    result_dict = {}
    for key in keys:
        result_dict[key] = []
        for dict in dicts:
            try:
                result_dict[key].append(dict[key])
            except KeyError:
                pass

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
print(combine_dicts(dicts))